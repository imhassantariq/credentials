# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-07-16 15:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0003_grades_username_mode_changes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usergrade',
            name='letter_grade',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
