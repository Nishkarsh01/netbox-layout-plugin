from django import forms
from netbox.forms import NetBoxModelForm
from utilities.forms.fields import DynamicModelChoiceField
from .models import RackArea
from dcim.models import Rack, Location

class RackAreaForm(NetBoxModelForm):
    """
    Form for creating and updating RackArea instances.
    """
    location = DynamicModelChoiceField(
        queryset=Location.objects.all(),
        required=True,
        help_text='Select the location for the rack area.'
    )
    rack = DynamicModelChoiceField(
        queryset=Rack.objects.none(),
        required=True,
        query_params={'location_id': '$location'},
        help_text='Select the rack within the chosen location.'
    )

    class Meta:
        """
        Meta options for the RackAreaForm.
        """
        model = RackArea
        fields = ('location', 'rack', 'top', 'left', 'width', 'height')

    def __init__(self, *args, **kwargs):
        """
        Initialize the form. If an instance is provided, set the rack queryset
        to only include racks within the instance's location.
        """
        super().__init__(*args, **kwargs)

        if self.instance and self.instance.pk:
            # If editing an existing instance, filter racks by the instance's location
            self.fields['rack'].queryset = Rack.objects.filter(location=self.instance.location)
        else:
            # If creating a new instance, start with an empty queryset for racks
            self.fields['rack'].queryset = Rack.objects.none()

        if 'location' in self.data:
            try:
                # Dynamically update the rack queryset based on the selected location
                location_id = int(self.data.get('location'))
                self.fields['rack'].queryset = Rack.objects.filter(location_id=location_id)
            except (ValueError, TypeError):
                # Handle invalid input gracefully by falling back to an empty queryset
                pass

    def clean(self):
        """
        Custom clean method to ensure the rack queryset is updated based on the selected location.
        """
        cleaned_data = super().clean()
        if cleaned_data is None:
            return cleaned_data

        location = cleaned_data.get('location')
        if location:
            # Update the rack queryset based on the cleaned location data
            self.fields['rack'].queryset = Rack.objects.filter(location=location)
        return cleaned_data
