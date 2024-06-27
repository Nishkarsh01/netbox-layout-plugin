# 003_auto_change_fields_to_float.py
from django.db import migrations, models
import django.core.validators

class Migration(migrations.Migration):

    dependencies = [
        ('netbox_layout_patch', '002_auto_change_fields_to_float'),  
    ]

    operations = [
        migrations.AlterField(
            model_name='rackarea',
            name='top',
            field=models.FloatField(
                validators=[
                    django.core.validators.MinValueValidator(0),
                    django.core.validators.MaxValueValidator(100)
                ],
                help_text='Top position in percentage (0-100)'
            ),
        ),
        migrations.AlterField(
            model_name='rackarea',
            name='left',
            field=models.FloatField(
                validators=[
                    django.core.validators.MinValueValidator(0),
                    django.core.validators.MaxValueValidator(100)
                ],
                help_text='Left position in percentage (0-100)'
            ),
        ),
        migrations.AlterField(
            model_name='rackarea',
            name='width',
            field=models.FloatField(
                validators=[
                    django.core.validators.MinValueValidator(0),
                    django.core.validators.MaxValueValidator(100)
                ],
                help_text='Width in percentage (0-100)'
            ),
        ),
        migrations.AlterField(
            model_name='rackarea',
            name='height',
            field=models.FloatField(
                validators=[
                    django.core.validators.MinValueValidator(0),
                    django.core.validators.MaxValueValidator(100)
                ],
                help_text='Height in percentage (0-100)'
            ),
        ),
    ]
