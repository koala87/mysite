# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Manual',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kind', models.CharField(max_length=10)),
                ('level', models.IntegerField()),
                ('title', models.TextField()),
                ('description', models.TextField(blank=True, null=True)),
                ('ltime', models.FloatField(blank=True, null=True)),
                ('mtime', models.FloatField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Objective',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='manual',
            name='obj',
            field=models.ManyToManyField(to='manual.Objective'),
        ),
    ]
