# Generated by Django 4.2.4 on 2023-08-15 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Building',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num_floors', models.IntegerField()),
                ('num_lifts', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Elevator',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField()),
                ('current_floor', models.IntegerField()),
                ('service_list', models.JSONField(default=list)),
                ('direction', models.IntegerField(default=0)),
                ('running', models.BooleanField(default=False)),
            ],
        ),
    ]
