from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from dcim.models import Rack, Location  # Assuming Location is defined in dcim.models
from django.urls import reverse
from netbox.models import NetBoxModel

class RackArea(NetBoxModel):
    """
    Model representing a specific area within a rack.
    """
    rack = models.OneToOneField(
        Rack,
        on_delete=models.CASCADE,
        help_text='The rack associated with this area.'
    )
    location = models.ForeignKey(
        Location,
        on_delete=models.CASCADE,
        help_text='The location of the rack area.'
    )
    top = models.FloatField(
        validators=[MinValueValidator(0), MaxValueValidator(100)],
        help_text='Top position in percentage (0-100).'
    )
    left = models.FloatField(
        validators=[MinValueValidator(0), MaxValueValidator(100)],
        help_text='Left position in percentage (0-100).'
    )
    width = models.FloatField(
        default=5.55,
        validators=[MinValueValidator(0), MaxValueValidator(100)],
        help_text='Width in percentage (0-100).'
    )
    height = models.FloatField(
        default=12.0,
        validators=[MinValueValidator(0), MaxValueValidator(100)],
        help_text='Height in percentage (0-100).'
    )

    def __str__(self):
        """
        String representation of the RackArea instance.
        """
        return f"RackArea for {self.rack} at ({self.top}%, {self.left}%) with size ({self.width}%, {self.height}%)"

    def get_absolute_url(self):
        """
        Returns the absolute URL for the RackArea instance.
        """
        return reverse('plugins:netbox_layout_patch:rackarea_list')

    class Meta:
        """
        Meta options for the RackArea model.
        """
        ordering = ['rack', 'top', 'left']
        verbose_name = 'Rack Area'
        verbose_name_plural = 'Rack Areas'
        constraints = [
            models.UniqueConstraint(fields=['rack'], name='unique_rack')
        ]
