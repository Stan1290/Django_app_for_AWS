# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-05 01:38
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('acc_views', '0002_auto_20171004_1951'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accounts',
            name='acc_description',
            field=models.CharField(max_length=1500),
        ),
        migrations.AlterField(
            model_name='accounts',
            name='balance',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='accounts',
            name='credit',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='accounts',
            name='debit',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='accounts',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='accounts',
            name='type',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='accounts',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='acc_views.Users'),
        ),
    ]
