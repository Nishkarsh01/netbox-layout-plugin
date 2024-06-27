from django.db import migrations, models
from django.core.validators import MinValueValidator, MaxValueValidator

class Migration(migrations.Migration):

    dependencies = [
        ('netbox_layout_patch', '006'),
    ]

    operations = [
        migrations.AddField(
            model_name='rackarea',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True, blank=True, verbose_name='created'),
        ),
        migrations.AddField(
            model_name='rackarea',
            name='last_updated',
            field=models.DateTimeField(auto_now=True, null=True, blank=True, verbose_name='last updated'),
        ),
        migrations.AlterModelOptions(
            name='rackarea',
            options={'verbose_name': 'Rack Area', 'verbose_name_plural': 'Rack Areas', 'ordering': ['rack', 'top', 'left']},
        ),
        migrations.AlterField(
            model_name='rackarea',
            name='top',
            field=models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(100)], help_text='Location in percentage (0-100)'),
        ),
        migrations.AlterField(
            model_name='rackarea',
            name='left',
            field=models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(100)], help_text='Left in percentage (0-100)'),
        ),
        migrations.AlterField(
            model_name='rackarea',
            name='width',
            field=models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(100)], help_text='Width in percentage (0-100)'),
        ),
        migrations.AlterField(
            model_name='rackarea',
            name='height',
            field=models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(100)], help_text='Height in percentage (0-100)'),
        ),
    ]
