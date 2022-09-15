# Generated by Django 4.1.1 on 2022-09-13 21:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='VisitorsExpoce',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('attend', models.CharField(max_length=100)),
                ('firstname', models.CharField(db_column='firstName', max_length=250)),
                ('lastname', models.CharField(db_column='lastName', max_length=250)),
                ('email', models.CharField(max_length=200)),
                ('age', models.CharField(max_length=10)),
                ('country', models.CharField(max_length=100)),
                ('cstate', models.CharField(db_column='cState', max_length=100)),
                ('phone', models.CharField(max_length=50)),
                ('languagelevel', models.CharField(db_column='languageLevel', max_length=50)),
                ('program', models.CharField(max_length=250)),
                ('studyarea', models.CharField(db_column='studyArea', max_length=100)),
                ('datestart', models.CharField(db_column='dateStart', max_length=100)),
                ('pay', models.CharField(max_length=100)),
                ('sourcelead', models.CharField(db_column='sourceLead', max_length=100)),
                ('fuente', models.CharField(max_length=100)),
                ('datetime', models.DateTimeField(db_column='dateTime')),
            ],
            options={
                'db_table': 'visitors_ExpoCE',
                'managed': False,
            },
        ),
    ]
