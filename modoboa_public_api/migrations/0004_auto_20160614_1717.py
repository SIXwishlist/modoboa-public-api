# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-14 17:17
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('modoboa_public_api', '0003_modoboaextension'),
    ]

    operations = [
        migrations.AddField(
            model_name='modoboainstance',
            name='alias_counter',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='modoboainstance',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2016, 6, 14, 17, 17, 37, 147971, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='modoboainstance',
            name='domain_counter',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='modoboainstance',
            name='extensions',
            field=models.ManyToManyField(blank=True, to='modoboa_public_api.ModoboaExtension'),
        ),
        migrations.AddField(
            model_name='modoboainstance',
            name='mailbox_counter',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='modoboainstance',
            name='ip_address',
            field=models.GenericIPAddressField(),
        ),
        migrations.AlterField(
            model_name='modoboainstance',
            name='last_request',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
