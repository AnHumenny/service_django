# Generated by Django 5.1.1 on 2024-11-27 11:23

import tinymce.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Fttx',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=30)),
                ('claster', models.CharField(max_length=30)),
                ('street', models.CharField(max_length=40)),
                ('number', models.CharField(max_length=10)),
                ('description', tinymce.models.HTMLField()),
                ('askue', models.GenericIPAddressField()),
            ],
            options={
                'verbose_name_plural': 'FttxX',
            },
        ),
    ]
