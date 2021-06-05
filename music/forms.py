from django.forms import ModelForm
from .models import Instrument

class InstrumentModelForm(ModelForm):
    class Meta:
        model = Instrument
        fields = ['title', 'history', 'poster', 'type']
        labels = {'title' : 'Název hudebního nástroje', 'history' : 'Historie hudebního nástroje', 'poster' : 'Obrázek', 'type' : 'Typ hudebního nástroje'}