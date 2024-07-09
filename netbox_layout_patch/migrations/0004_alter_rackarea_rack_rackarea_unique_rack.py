# Generated by Django 5.0.6 on 2024-07-02 20:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dcim', '0187_alter_device_vc_position'),
        ('extras', '0115_convert_dashboard_widgets'),
        ('netbox_layout_patch', '0003_rackarea_custom_field_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rackarea',
            name='rack',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='dcim.rack'),
        ),
        migrations.AddConstraint(
            model_name='rackarea',
            constraint=models.UniqueConstraint(fields=('rack',), name='unique_rack'),
        ),
    ]
