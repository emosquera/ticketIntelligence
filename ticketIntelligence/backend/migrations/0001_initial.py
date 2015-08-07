# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.TextField(max_length=100, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateField(null=True, blank=True)),
                ('number', models.IntegerField(default=None, null=True)),
                ('serie', models.CharField(max_length=90)),
                ('object_id', models.PositiveIntegerField(null=True, verbose_name=b'related object')),
                ('status', models.CharField(max_length=20, choices=[(b'Atendido', b'ATENDIDO'), (b'Cancelado', b'CANCELADO'), (b'Pendiente', b'PENDIENTE')])),
                ('content_type', models.ForeignKey(verbose_name=b'content type', blank=True, to='contenttypes.ContentType', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('type', models.CharField(max_length=20, choices=[(b'Branch', b'BRANCH'), (b'Company', b'COMPANY'), (b'Costumer', b'COSTUMER'), (b'Franchise', b'FRANCHISE')])),
            ],
        ),
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('userprofile_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='backend.UserProfile')),
                ('nickName', models.CharField(max_length=300)),
                ('address', models.TextField(max_length=1000, blank=True)),
                ('phone', models.TextField(max_length=20, blank=True)),
            ],
            bases=('backend.userprofile',),
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('userprofile_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='backend.UserProfile')),
                ('name', models.TextField(max_length=100, blank=True)),
                ('identityDoc', models.CharField(unique=True, max_length=12)),
                ('address', models.TextField(max_length=1000, blank=True)),
                ('phone', models.TextField(max_length=20, blank=True)),
            ],
            bases=('backend.userprofile',),
        ),
        migrations.CreateModel(
            name='Costumer',
            fields=[
                ('userprofile_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='backend.UserProfile')),
                ('name', models.TextField(max_length=100, blank=True)),
                ('lastName', models.TextField(max_length=100, blank=True)),
                ('address', models.TextField(max_length=1000, blank=True)),
                ('identityDoc', models.IntegerField(unique=True)),
                ('homePhone', models.TextField(max_length=20, blank=True)),
                ('cellPhone', models.TextField(max_length=20, blank=True)),
                ('email', models.EmailField(max_length=254)),
            ],
            bases=('backend.userprofile',),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='user',
            field=models.OneToOneField(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='city',
            name='state',
            field=models.ForeignKey(to='backend.State'),
        ),
        migrations.CreateModel(
            name='Franchise',
            fields=[
                ('company_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='backend.Company')),
                ('brand', models.ForeignKey(to='backend.Brand')),
            ],
            bases=('backend.company',),
        ),
        migrations.AddField(
            model_name='company',
            name='city',
            field=models.ForeignKey(to='backend.City'),
        ),
        migrations.AddField(
            model_name='branch',
            name='city',
            field=models.ForeignKey(to='backend.City'),
        ),
        migrations.AddField(
            model_name='branch',
            name='company',
            field=models.ForeignKey(to='backend.Company'),
        ),
    ]
