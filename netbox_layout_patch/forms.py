# forms.py
from django import forms
from .models import RackArea

class RackAreaForm(forms.ModelForm):

    class Meta:
        model = RackArea
        fields = ['rack', 'top', 'left', 'width', 'height']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


