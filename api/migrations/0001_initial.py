# Generated by Django 5.1.1 on 2024-11-27 11:23

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='InfoLastMonth',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateField(default=django.utils.timezone.now)),
                ('city', models.CharField(max_length=20)),
                ('street', models.CharField(max_length=30)),
                ('home', models.CharField(max_length=7)),
                ('apartment', models.CharField(max_length=4)),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'info_info',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SearchKey',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=20)),
                ('street', models.CharField(max_length=30)),
                ('home', models.CharField(max_length=7)),
                ('entrance', models.IntegerField()),
                ('ind', models.IntegerField()),
                ('stand', models.IntegerField()),
            ],
            options={
                'db_table': 'key_key',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=150)),
                ('first_name', models.CharField(max_length=150)),
                ('last_name', models.CharField(max_length=150)),
                ('email', models.EmailField(max_length=254, unique=True)),
            ],
            options={
                'db_table': 'auth_user',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='InfoPreviosMonth',
            fields=[
                ('infolastmonth_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='api.infolastmonth')),
            ],
            bases=('api.infolastmonth',),
        ),
    ]