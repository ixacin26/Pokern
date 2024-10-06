from django.contrib import admin
from .models import Spieler, Event, EventTeilnahme #,ChipTransaktion
from .forms import EventTeilnahmeForm  # Importiere das benutzerdefinierte Formular

class EventTeilnahmeAdmin(admin.ModelAdmin):
    form = EventTeilnahmeForm  # Verwende das benutzerdefinierte Formular für EventTeilnahme

admin.site.register(Spieler)
admin.site.register(Event)
#admin.site.register(ChipTransaktion)
admin.site.register(EventTeilnahme, EventTeilnahmeAdmin)  # Registriere die EventTeilnahme mit dem neuen Admin
