# Generated by Django 3.2.3 on 2021-06-20 07:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('model', '0011_alter_bitcoin_table'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='bitcoin',
            table='price',
        ),
    ]
