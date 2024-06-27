
from django.db import migrations, models
import django.db.models.deletion

class Migration(migrations.Migration):

    dependencies = [
        ('netbox_layout_patch', '004_auto_add_location_field'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rackarea',
            name='location',
        ),
    ]
