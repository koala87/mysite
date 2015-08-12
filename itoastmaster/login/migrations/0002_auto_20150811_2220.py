# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='status',
            field=models.CharField(blank=True, max_length=16, null=True),
        ),
    ]
