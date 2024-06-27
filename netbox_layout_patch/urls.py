from django.urls import path
from . import views


urlpatterns = [
    path('rack_areas/', views.RackAreaListView.as_view(), name='rackarea_list'),
    path('rack_areas/delete/<int:pk>/', views.RackAreaDeleteView.as_view(), name='rackarea_delete'),
    path('rack_areas/edit/<int:pk>/', views.RackAreaEditView.as_view(), name='rackarea_edit'),

]
