# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-04-13 11:38
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_calc_author'),
        ('blog', '0006_auto_20160312_1436'),
        ('admin', '0002_logentry_remove_auto_add'),
        ('sbersignal', '0011_auto_20160410_1818'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='user_ptr',
        ),
        migrations.DeleteModel(
            name='UserProfile',
        ),
    ]