# Generated by Django 4.2.3 on 2023-07-28 05:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0004_property_latitude'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='property',
            name='latitude',
        ),
        migrations.RemoveField(
            model_name='property',
            name='longitude',
        ),
    ]
