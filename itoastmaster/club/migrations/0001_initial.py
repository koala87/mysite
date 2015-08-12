# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Club',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('time', models.TextField(blank=True, null=True)),
                ('week', models.IntegerField(blank=True, null=True)),
                ('addr', models.TextField(blank=True, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('phone', models.CharField(blank=True, max_length=64, null=True)),
                ('website', models.TextField(blank=True, null=True)),
                ('geo_longitude', models.FloatField(blank=True, null=True)),
                ('geo_latitude', models.FloatField(blank=True, null=True)),
                ('country_id', models.IntegerField(blank=True, null=True)),
                ('zones_id', models.IntegerField(blank=True, null=True)),
                ('city_id', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]
