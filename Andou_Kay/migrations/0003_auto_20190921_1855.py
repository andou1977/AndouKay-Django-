# Generated by Django 2.2.4 on 2019-09-22 01:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Andou_Kay', '0002_auto_20190921_0146'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proprietaire',
            name='Cout',
            field=models.CharField(max_length=50),
        ),
    ]
