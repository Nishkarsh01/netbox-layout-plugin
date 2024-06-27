from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('netbox_layout_patch', '005_auto_remove_location_filed'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='rackarea',
            options={'verbose_name': 'Rack Area', 'verbose_name_plural': 'Rack Areas', 'ordering': ['rack', 'top', 'left']},
        ),
    ]
