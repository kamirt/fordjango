# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-04-09 11:32
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('sbersignal', '0004_auto_20160409_1715'),
    ]

    operations = [
        migrations.AddField(
            model_name='recommendation',
            name='date_of_rec_ex',
            field=models.DateTimeField(default=datetime.datetime(2016, 4, 9, 11, 32, 55, 140096, tzinfo=utc), verbose_name='По'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='recommendation',
            name='date_of_rec',
            field=models.DateTimeField(verbose_name='C'),
        ),
    ]