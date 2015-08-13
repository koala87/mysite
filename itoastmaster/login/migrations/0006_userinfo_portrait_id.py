# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0005_province1_school'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='portrait_id',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
