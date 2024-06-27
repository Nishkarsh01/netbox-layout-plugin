# netbox_layout_plugin/migrations/0001_initial.py
from django.db import migrations, models
import django.db.models.deletion

class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('dcim', '0187_alter_device_vc_position'),  # replace 'latest_migration_file' with the actual latest migration
    ]

    operations = [
        migrations.CreateModel(
            name='RackArea',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('top', models.PositiveIntegerField()),
                ('left', models.PositiveIntegerField()),
                ('width', models.PositiveIntegerField()),
                ('height', models.PositiveIntegerField()),
                ('rack', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='rack_area', to='dcim.Rack')),
            ],
        ),
    ]

