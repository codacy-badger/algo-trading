# Generated by Django 4.1.5 on 2023-04-04 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('algo_trading', '0007_ohlcvdatadaily_ohlcvdatadaily_ohlcv_daily_date_idx_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ohlcvdatadaily',
            name='dividends',
        ),
        migrations.RemoveField(
            model_name='ohlcvdatadaily',
            name='splits',
        ),
        migrations.RemoveField(
            model_name='ohlcvdatadaily',
            name='volume',
        ),
        migrations.AddField(
            model_name='instrument',
            name='zerodha_exchange',
            field=models.CharField(default='', max_length=50, verbose_name='zerdoha exchange'),
        ),
        migrations.AddField(
            model_name='instrument',
            name='zerodha_exchange_token',
            field=models.CharField(default='', max_length=50, verbose_name='zerodha exchange token'),
        ),
        migrations.AddField(
            model_name='instrument',
            name='zerodha_instrument_token',
            field=models.IntegerField(default=0, verbose_name='zerodha instrument token'),
        ),
        migrations.AddField(
            model_name='instrument',
            name='zerodha_lot_size',
            field=models.IntegerField(default=0, verbose_name='zerodha lot size'),
        ),
        migrations.AddField(
            model_name='instrument',
            name='zerodha_segment',
            field=models.CharField(default='', max_length=50, verbose_name='zerodha segment'),
        ),
        migrations.AddField(
            model_name='instrument',
            name='zerodha_trading_symbol',
            field=models.CharField(default='', max_length=50, verbose_name='zerodha trading symbol'),
        ),
        migrations.AddField(
            model_name='ohlcvdatadaily',
            name='last_price',
            field=models.DecimalField(decimal_places=5, default=0.0, max_digits=15, verbose_name='last price'),
        ),
    ]