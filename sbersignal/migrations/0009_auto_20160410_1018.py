# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-04-10 03:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sbersignal', '0008_auto_20160410_1008'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recommendation',
            name='rec',
            field=models.CharField(choices=[('buy', 'Покупка'), ('sell', 'Продажа')], default='buy', max_length=100, verbose_name='Сигнал'),
        ),
    ]
