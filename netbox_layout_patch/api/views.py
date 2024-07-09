# api/views.py
from netbox.api.viewsets import NetBoxModelViewSet
from ..models import RackArea
from .serializers import RackAreaSerializer

class RackAreaViewSet(NetBoxModelViewSet):
    queryset = RackArea.objects.all()
    serializer_class = RackAreaSerializer
