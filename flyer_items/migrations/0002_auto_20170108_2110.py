# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-08 21:10
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flyer_items', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='flyeritem',
            old_name='grocery',
            new_name='store',
        ),
    ]
