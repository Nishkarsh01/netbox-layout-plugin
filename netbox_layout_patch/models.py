from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from dcim.models import Rack
from django.db.models import QuerySet
from django.urls import reverse
from netbox.models import NetBoxModel

from netbox.models.features import ChangeLoggingMixin

class RestrictedQuerySet(QuerySet):
    def restrict(self, user, action):

        if user.has_perm('netbox_layout_patch.view_rackarea'):
            return self.all()  # Return all objects if user has permission
        else:
            return self.none()  # Return empty queryset if user doesn't have permission

class RackArea(NetBoxModel):
    rack = models.ForeignKey(Rack, on_delete=models.CASCADE)
    top = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(100)], help_text='Location in percentage (0-100)')
    left = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(100)], help_text='Left in percentage (0-100)')
    width = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(100)], help_text='Width in percentage (0-100)')
    height = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(100)], help_text='Height in percentage (0-100)')

    objects = RestrictedQuerySet.as_manager()  # Set RestrictedQuerySet as default manager

    custom_field_data = 'blank'
    
    def __str__(self):
        return f"RackArea for {self.rack} at ({self.top}, {self.left}) size ({self.width}, {self.height})"

    class Meta:
        verbose_name = 'Rack Area'
        verbose_name_plural = 'Rack Areas'
        ordering = ['rack', 'top', 'left']
    
    
    