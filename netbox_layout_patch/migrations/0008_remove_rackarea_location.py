# Generated by Django 5.0.6 on 2024-07-03 13:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('netbox_layout_patch', '0007_rackarea_location'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rackarea',
            name='location',
        ),
    ]
