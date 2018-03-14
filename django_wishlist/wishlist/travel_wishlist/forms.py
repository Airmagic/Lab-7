from django import forms
from .models import Place

# makes new items for the list
class NewPlaceForm(forms.ModelForm):
    class Meta:
        model = Place
        fields = ('name', 'visited')
