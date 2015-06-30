# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Donator',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('phone', models.CharField(unique=True, max_length=20)),
                ('address', models.TextField()),
                ('slug', models.SlugField(unique=True)),
                ('blood_type', models.CharField(default=b'A', max_length=4, choices=[(b'A', b'A+'), (b'B', b'A-'), (b'C', b'B+'), (b'D', b'B-'), (b'E', b'AB+'), (b'F', b'AB-'), (b'G', b'O+'), (b'H', b'O-')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
