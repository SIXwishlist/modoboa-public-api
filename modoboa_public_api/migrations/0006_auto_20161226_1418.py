# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-12-26 13:18
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('modoboa_public_api', '0005_modoboainstance_domain_alias_counter'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='modoboainstance',
            unique_together=set([]),
        ),
    ]