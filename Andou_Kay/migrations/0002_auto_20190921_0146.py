# Generated by Django 2.2.4 on 2019-09-21 08:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Andou_Kay', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='proprietaire',
            name='Latitude',
        ),
        migrations.RemoveField(
            model_name='proprietaire',
            name='Longitude',
        ),
    ]