# tables.py

import django_tables2 as tables
from netbox.tables import NetBoxTable
from .models import RackArea

class RackAreaTable(NetBoxTable):
    """
    Table for displaying Rack Area information.
    """
    rack = tables.Column(linkify=True)
    location = tables.Column(linkify=True, accessor='rack.location')

    class Meta(NetBoxTable.Meta):
        """
        Meta options for the RackAreaTable.
        """
        model = RackArea
        fields = ('pk', 'id', 'rack', 'location', 'top', 'left', 'width', 'height')
        default_columns = ('pk', 'rack', 'location', 'top', 'left', 'width', 'height')
