# 004_auto_add_location_field.py
from django.db import migrations, models
import django.db.models.deletion

class Migration(migrations.Migration):

    dependencies = [
        ('netbox_layout_patch', '003_auto_change_fields_to_float'),
        ('dcim', '0187_alter_device_vc_position'),  
    ]

    operations = [
        migrations.AddField(
            model_name='rackarea',
            name='location',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to='dcim.Location',
                default=1  # Adjust the default value as necessary
            ),
            preserve_default=False,
        ),
    ]
