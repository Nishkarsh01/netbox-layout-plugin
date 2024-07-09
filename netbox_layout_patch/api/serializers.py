# api/serializers.py
from rest_framework import serializers
from netbox.api.serializers import NetBoxModelSerializer
from ..models import RackArea

class RackAreaSerializer(NetBoxModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='plugins-api:netbox_layout_patch-api:rackarea-detail'
    )

    class Meta:
        model = RackArea
        fields = '__all__'
