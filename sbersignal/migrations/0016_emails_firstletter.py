# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-04-18 11:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sbersignal', '0015_auto_20160418_1826'),
    ]

    operations = [
        migrations.CreateModel(
            name='Emails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=200)),
                ('text', models.TextField()),
            ],
            options={
                'verbose_name': 'Рассылка',
                'verbose_name_plural': 'Рассылки',
            },
        ),
        migrations.CreateModel(
            name='FirstLetter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=200)),
                ('text', models.TextField()),
            ],
            options={
                'verbose_name': 'Первое_письмо',
                'verbose_name_plural': 'Первые_письма',
            },
        ),
    ]