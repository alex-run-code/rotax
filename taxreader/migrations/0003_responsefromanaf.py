# Generated by Django 3.0.7 on 2020-06-22 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taxreader', '0002_auto_20200620_1434'),
    ]

    operations = [
        migrations.CreateModel(
            name='ResponseFromAnaf',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now=True)),
                ('data_sent', models.CharField(max_length=1000)),
                ('data_received', models.CharField(max_length=10000)),
                ('status_code', models.IntegerField()),
            ],
        ),
    ]