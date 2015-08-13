# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0006_userinfo_portrait_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='born',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='userinfo',
            name='phone',
            field=models.TextField(blank=True, null=True),
        ),
    ]
