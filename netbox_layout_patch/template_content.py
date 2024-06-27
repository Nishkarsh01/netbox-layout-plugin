from dcim.models.racks import Rack
from netbox.plugins import PluginTemplateExtension
from .models import RackArea

class RackAreaTemplateLocationView(PluginTemplateExtension):
    model = 'dcim.location'

    def right_page(self):
        instance = self.context['object']
        location_ids = instance.get_descendants(include_self=True).values_list('pk', flat=True)
        racks = Rack.objects.filter(location__in=location_ids)
        layout_areas = []
        
        for rack in racks:
            rack_areas = RackArea.objects.filter(rack=rack)
            for area in rack_areas:
                layout_area = {
                    "pk": rack.pk,
                    "name": rack.name,
                    "left": area.left,
                    "top": area.top,
                    "width": area.width,
                    "height": area.height
                }
                layout_areas.append(layout_area)
        
        return self.render('netbox_layout_patch/layouts_tab.html', extra_context={
            'layout_areas': layout_areas
        })
    
class RackAreaTemplateRackView(PluginTemplateExtension):
    model = 'dcim.rack'

    def right_page(self):
        rack = self.context['object']
        rack_areas = RackArea.objects.filter(rack=rack)
        return self.render('netbox_layout_patch/rack_area_inject.html', extra_context={
            'rack_areas': rack_areas
        })

template_extensions = [RackAreaTemplateLocationView, RackAreaTemplateRackView]
