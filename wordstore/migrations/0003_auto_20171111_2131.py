# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-12 00:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wordstore', '0002_word_url_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='word',
            name='url_imagen',
            field=models.CharField(default='http://www.upforest.gov.in/Images/Default.png', max_length=200),
        ),
    ]
