# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('club', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=100)),
                ('portrait', models.CharField(blank=True, max_length=100, null=True)),
                ('sex', models.CharField(blank=True, max_length=8, null=True)),
                ('status', models.CharField(max_length=16, null=True)),
                ('lovebridge', models.BooleanField()),
                ('hometown', models.TextField(blank=True, null=True)),
                ('school', models.TextField(blank=True, null=True)),
                ('join_dt', models.DateField(blank=True, null=True)),
                ('progress', models.TextField(blank=True, null=True)),
                ('positions', models.TextField(blank=True, null=True)),
                ('interest', models.TextField(blank=True, null=True)),
                ('self_introduction', models.TextField(blank=True, null=True)),
                ('word', models.TextField(blank=True, null=True)),
                ('club', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='club.Club')),
            ],
        ),
    ]
