# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-21 06:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=200)),
                ('nioss', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Organisation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('contract', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('contact_phone', models.CharField(max_length=100)),
                ('contact_mail', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='People',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('contact_phone', models.CharField(max_length=100)),
                ('contact_mail', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=100)),
                ('employer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Organisation')),
            ],
        ),
        migrations.CreateModel(
            name='Port',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=100)),
                ('device', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Device')),
            ],
        ),
        migrations.AddField(
            model_name='location',
            name='contact',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.People'),
        ),
        migrations.AddField(
            model_name='device',
            name='location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Location'),
        ),
    ]
