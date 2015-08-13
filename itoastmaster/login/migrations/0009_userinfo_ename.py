# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0008_auto_20150813_2152'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='ename',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
