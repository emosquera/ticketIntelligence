# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0007_auto_20150804_1906'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='address',
            field=models.TextField(max_length=1000, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='cellPhone',
            field=models.TextField(max_length=20, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='homePhone',
            field=models.TextField(max_length=20, null=True, blank=True),
        ),
    ]
