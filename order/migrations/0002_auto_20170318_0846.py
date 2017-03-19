# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2017-03-18 08:46
from __future__ import unicode_literals

from django.db import migrations, models
import order.models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='productModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kitId', models.CharField(default='00000000', max_length=8, unique=True)),
                ('price', models.FloatField()),
            ],
        ),
        migrations.AlterField(
            model_name='ordermodel',
            name='city',
            field=models.CharField(max_length=100, validators=[order.models.validate_city]),
        ),
        migrations.AlterField(
            model_name='ordermodel',
            name='county',
            field=models.CharField(max_length=100, validators=[order.models.validate_county]),
        ),
        migrations.AlterField(
            model_name='ordermodel',
            name='invoice',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='ordermodel',
            name='province',
            field=models.CharField(max_length=20, validators=[order.models.validate_province]),
        ),
    ]
