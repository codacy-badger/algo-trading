import datetime
import re

from django.db import models
from django.db.models import Q
from django.db.models.query import QuerySet

from ..instruments import Instrument


class TradingSignalManager(models.Manager):
    """Manager class for `TradingSignal`

    Class level functionalities for trading signal go here
    """

    def create_from_call_blob(self, call_blob: str):
        """Creates a TradingSignal from an options call

        Parses the call from the below format and creates attributes for the object.
        Fetches the instrument name as received from the available set of instruments
        Raises 404 error if the instrument is not tradeable.

        Parameters
        ----------
        call_blob: str
            The call for options as received
            Sample:
            MANAPPURAM JUN 110 CE
            Entry -  5.20
            Targets -  5.70, 10+
            Stoploss -  2.50
            The format always remains the same for options call

        Returns
        -------
        TradingSignal object created out of the received call for the instrument
        along with other details from the instrument

        Raises
        ------
        Http404 if the instrument does not exist in the DB for trading.
        """

        lines = call_blob.split("\r\n")

        instrument_name = lines[0].strip()
        entry_line = lines[1].strip()
        targets_line = lines[2].strip()
        stoploss_line = lines[3].strip()

        entry_point = re.search(r"Entry - (.*)", entry_line)[1].strip()
        stoploss_point = re.search(r"Stoploss - (.*)", stoploss_line)[1].strip()
        targets = re.search(r"Targets - (.*)", targets_line)[1].strip()
        target1, target2 = [x.strip() for x in targets.split(",")]
        target2 = re.search(r"(.*)\+", target2)[1]

        option_type = instrument_name[-2:]

        instrument = Instrument.objects.get_options_from_symbol(instrument_name)

        signal = self.create(
            signal_type=self.model.TradingSignalType.BUY,
            instrument_type=option_type,
            entry_point=entry_point,
            stoploss_point=stoploss_point,
            target1=target1,
            target2=target2,
            lot_size=instrument.lot_size,
            tick_size=instrument.tick_size,
            instrument=instrument,
            created_at=datetime.datetime.now(),
            signal_source="Praveen Calls",
        )

        return signal

    def get_options_calls(self) -> QuerySet:
        """Return all options calls"""

        return (
            super()
            .get_queryset()
            .filter(
                Q(instrument_type=Instrument.InstrumentType.CALL_OPTION)
                | Q(instrument_type=Instrument.InstrumentType.PUT_OPTION)
            )
        )
