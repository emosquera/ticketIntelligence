# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0005_auto_20150728_1539'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='branch',
            options={'permissions': (('is_branch', 'Es una sucursal'),)},
        ),
        migrations.AlterModelOptions(
            name='company',
            options={'permissions': (('is_company', 'Es una empresa'),)},
        ),
        migrations.AlterModelOptions(
            name='customer',
            options={'permissions': (('is_customer', 'Es un cliente'),)},
        ),
        migrations.AlterModelOptions(
            name='franchise',
            options={'permissions': (('is_franchise', 'Es una franquicia'),)},
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='type',
            field=models.CharField(max_length=20, choices=[(b'Branch', b'BRANCH'), (b'Company', b'COMPANY'), (b'Customer', b'CUSTOMER'), (b'Franchise', b'FRANCHISE')]),
        ),
    ]
