# Generated by Django 5.0.6 on 2024-07-03 14:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('netbox_layout_patch', '0009_rackarea_location'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rackarea',
            name='location',
        ),
    ]
