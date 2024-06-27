from django.shortcuts import render, get_object_or_404, redirect
from netbox.views import generic
from .models import RackArea
from .forms import RackAreaForm
from .tables import RackAreaTable
import logging

logger = logging.getLogger(__name__)

class RackAreaListView(generic.ObjectListView):
    queryset = RackArea.objects.all()
    template_name = 'netbox_layout_patch/rackarea_list.html'
    table = RackAreaTable

class RackAreaEditView(generic.ObjectEditView):
    queryset = RackArea.objects.all()
    template_name = 'netbox_layout_patch/rackarea_edit.html'

class RackAreaDeleteView(generic.ObjectDeleteView):
    queryset = RackArea.objects.all()
    template_name = 'netbox_layout_patch/rackarea_delete.html'



