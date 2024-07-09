from dcim.models.racks import Rack
from netbox.plugins import PluginTemplateExtension
from .models import RackArea
from dcim.models import Location


class RackAreaTemplateLocationView(PluginTemplateExtension):
    """
    Template extension to inject custom content into the Location detail view.
    This extension adds information about rack areas within the location.
    """
    model = 'dcim.location'

    def right_page(self):
        """
        Renders the custom content to be injected into the right side of the Location detail view.
        Retrieves and displays rack areas for all racks within the current location and its descendants.

        Returns:
            str: Rendered HTML content.
        """
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

        return self.render('netbox_layout_patch/rackarea_layouts_tab.html', extra_context={
            'layout_areas': layout_areas
        })


class RackAreaTemplateRackView(PluginTemplateExtension):
    """
    Template extension to inject custom content into the Rack detail view.
    This extension adds information about rack areas within the specific rack.
    """
    model = 'dcim.rack'

    def right_page(self):
        """
        Renders the custom content to be injected into the right side of the Rack detail view.
        Retrieves and displays rack areas for the current rack.

        Returns:
            str: Rendered HTML content.
        """
        rack = self.context['object']
        rack_areas = RackArea.objects.filter(rack=rack)

        return self.render('netbox_layout_patch/rack_area_inject.html', extra_context={
            'rack_areas': rack_areas
        })

class RackAreaTemplateEditView(PluginTemplateExtension):
    model = 'netbox_layout_patch.rackarea'

    def right_page(self):
        return self.render('netbox_layout_patch/rackarea_preview.html')

# Register the template extensions
template_extensions = [RackAreaTemplateLocationView, RackAreaTemplateRackView, RackAreaTemplateEditView]
