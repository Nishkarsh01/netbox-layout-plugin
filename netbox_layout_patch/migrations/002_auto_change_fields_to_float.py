from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('netbox_layout_patch', '001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rackarea',
            name='top',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='rackarea',
            name='left',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='rackarea',
            name='width',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='rackarea',
            name='height',
            field=models.FloatField(),
        ),
    ]
