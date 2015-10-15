# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='DIC',
            new_name='IDC',
        ),
        migrations.AlterModelOptions(
            name='idc',
            options={'verbose_name': 'IDC', 'verbose_name_plural': 'IDC'},
        ),
    ]
