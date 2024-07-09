import logging
import requests

from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import View
from netbox.views import generic
from netbox.views.generic import ObjectChangeLogView
from django.db.models import Q
from extras.models import ImageAttachment

from .models import RackArea
from .forms import RackAreaForm
from .tables import RackAreaTable
from django.http import JsonResponse
from dcim.models import Location

# Initialize logger
logger = logging.getLogger(__name__)

class RackAreaListView(generic.ObjectListView):
    """
    View for listing all Rack Areas.
    """
    queryset = RackArea.objects.all()
    table = RackAreaTable

    def get_queryset(self, *args, **kwargs):
        """
        Override the default get_queryset method to add search functionality.
        Filters the queryset based on the search query provided in the request.
        """
        queryset = super().get_queryset(*args, **kwargs)
        search = self.request.GET.get('q')
        if search:
            queryset = queryset.filter(
                Q(location__name__icontains=search) | Q(rack__name__icontains=search)
            )
        return queryset

class RackAreaEditView(generic.ObjectEditView):
    """
    View for creating and editing a Rack Area.
    """
    queryset = RackArea.objects.all()
    form = RackAreaForm
    template_name = 'netbox_layout_patch/rackarea_preview.html'


class RackAreaDeleteView(generic.ObjectDeleteView):
    """
    View for deleting a Rack Area.
    """
    queryset = RackArea.objects.all()

class RackAreaChangeLogView(ObjectChangeLogView):
    """
    View for displaying the change log of a Rack Area.
    """
    base_template = 'dcim/device/base.html'


def get_location_image(request, location_id):
    """
    Retrieve the URL of the first image attachment with "Layout" in its URL for a given location.

    Args:
        request (HttpRequest): The HTTP request object.
        location_id (int): The ID of the location for which to retrieve the image.

    Returns:
        JsonResponse: A JSON response containing the image URL or an error message.
    """
    try:
        # Ensure the location exists
        location = Location.objects.get(pk=location_id)

        # Get all ImageAttachment objects for the location
        image_attachments = ImageAttachment.objects.filter(object_id=location_id)

        # Find the first image with "Layout" in its URL
        for image_attachment in image_attachments:
            if 'Layout' in image_attachment.image.url:
                return JsonResponse({'image_url': image_attachment.image.url})

        # If no image with "Layout" in its URL is found, return an error response
        return JsonResponse({'error': 'No image found for the selected location.'}, status=404)
    except Location.DoesNotExist:
        # If the location does not exist, return an error response
        return JsonResponse({'error': 'Invalid location ID.'}, status=400)
