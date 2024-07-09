# Generated by Django 5.0.6 on 2024-07-03 14:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dcim', '0187_alter_device_vc_position'),
        ('netbox_layout_patch', '0008_remove_rackarea_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='rackarea',
            name='location',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='dcim.location'),
            preserve_default=False,
        ),
    ]
