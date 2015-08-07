# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='costumer',
            name='city',
            field=models.ForeignKey(default=1, to='backend.City'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='city',
            name='state',
            field=models.ForeignKey(related_name='cities', to='backend.State'),
        ),
    ]
