# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('dt', models.DateField()),
                ('time', models.TimeField()),
                ('name', models.TextField()),
                ('secrect', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.TextField()),
                ('name', models.TextField()),
                ('title', models.TextField()),
                ('content', models.TextField(blank=True)),
                ('dt', models.DateField()),
                ('time', models.TimeField()),
                ('raw_time', models.FloatField()),
                ('display', models.BooleanField()),
                ('comments', models.ManyToManyField(to='news.Comment')),
            ],
        ),
    ]
