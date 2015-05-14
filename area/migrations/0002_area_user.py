# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('area', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('area_map', models.ForeignKey(to='area.Area_map')),
                ('description', models.ForeignKey(to='area.Description')),
                ('quest', models.ForeignKey(to='area.Quest')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=250)),
                ('character', models.CharField(max_length=250)),
                ('email', models.EmailField(max_length=254)),
                ('passwd', models.CharField(max_length=250)),
            ],
        ),
    ]
