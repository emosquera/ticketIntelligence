# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0002_auto_20150727_2108'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Costumer',
            new_name='Customer',
        ),
        migrations.AlterField(
            model_name='ticket',
            name='status',
            field=models.CharField(max_length=20, choices=[(b'Attended', b'ATTENDED'), (b'Canceled', b'CANCEL'), (b'Pending', b'PENDING')]),
        ),
    ]
