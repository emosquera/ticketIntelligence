# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0003_auto_20150728_1418'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='city',
            field=models.ForeignKey(related_name='city', to='backend.City'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='user',
            field=models.OneToOneField(related_name='user', to=settings.AUTH_USER_MODEL),
        ),
    ]
