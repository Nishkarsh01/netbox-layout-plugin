import django_tables2 as tables
from netbox.tables import NetBoxTable
from .models import RackArea

class RackAreaTable(NetBoxTable):
    rack = tables.Column(linkify=True)
    location = tables.Column(linkify=True, accessor='rack.location')

    class Meta(NetBoxTable.Meta):
        model = RackArea
        fields = ('pk', 'id', 'rack', 'location', 'top', 'left', 'width', 'height')
        default_columns = ('pk', 'rack', 'location', 'top', 'left', 'width', 'height')
