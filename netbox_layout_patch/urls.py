# urls.py

from django.urls import path
from .models import RackArea
from .views import (
    RackAreaListView,
    RackAreaEditView,
    RackAreaDeleteView,
    RackAreaChangeLogView,
    get_location_image
)


# Define URL patterns for RackArea views
urlpatterns = [
    path(
        'rack_areas/',
        RackAreaListView.as_view(),
        name='rackarea_list'
    ),
    path(
        'rack_areas/add/',
        RackAreaEditView.as_view(),
        name='rackarea_add'
    ),
    path(
        'rack_areas/<int:pk>/edit/',
        RackAreaEditView.as_view(),
        name='rackarea_edit'
    ),
    path(
        'rack_areas/<int:pk>/delete/',
        RackAreaDeleteView.as_view(),
        name='rackarea_delete'
    ),
    path(
        'rack_areas/<int:pk>/changelog/',
        RackAreaChangeLogView.as_view(),
        name='rackarea_changelog',
        kwargs={'model': RackArea}
    ),
    path(
        'api/location-image/<int:location_id>/',
        get_location_image,
        name='get_location_image'
    ),
]
