# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='area_map',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('map_field', models.TextField()),
                ('notes', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='description',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('description_text', models.TextField()),
                ('pub_date', models.DateTimeField(verbose_name=b'date published')),
                ('submitter', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='quest',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('description_text', models.TextField()),
            ],
        ),
    ]
