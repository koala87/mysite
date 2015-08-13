# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0007_auto_20150813_2148'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userinfo',
            old_name='progress',
            new_name='leader',
        ),
        migrations.AddField(
            model_name='userinfo',
            name='speech',
            field=models.TextField(blank=True, null=True),
        ),
    ]
