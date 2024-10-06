from django import forms
from .models import EventTeilnahme, Event

class EventTeilnahmeForm(forms.ModelForm):
    class Meta:
        model = EventTeilnahme
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Filtere nur aktive Events
        self.fields['event'].queryset = Event.objects.filter(active=True)