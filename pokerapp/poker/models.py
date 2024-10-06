from django.db import models
from django.core.exceptions import ValidationError

class Spieler(models.Model):
    name = models.CharField(max_length=100)
    gesamtgewinn = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    gruendungsmitglied = models.BooleanField(default=False)
    date_of_first_participation = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.name

class Event(models.Model):
    # Gastgebereinstellungen
    asop = models.BooleanField(default=False)  #Kennzeichnet ein Event als ASOP, womit kein Gastgeber_Spieler notwendig ist
    gastgeber_spieler = models.ForeignKey(Spieler, on_delete=models.SET_NULL, blank=True, null=True, related_name='gastgeber_events')  # Auswahl eines Spielers
    teilnehmer = models.ManyToManyField(Spieler, through='EventTeilnahme', related_name='teilnahmen')
    pot = models.DecimalField(max_digits=10, decimal_places=2) #maximale Chips die aus dem Koffer gekauft werden können
    datum = models.DateField() #Dataum des Events
    active = models.BooleanField(default=True)  #Event hat geendet (false) oder läuft noch (true)
    
    

    def clean(self):
        # Custom validation to ensure either `asop` is True or `gastgeber_spieler` is provided
        if not self.asop and not self.gastgeber_spieler:
            raise ValidationError("Entweder muss ASOP aktiviert sein oder ein Spieler ausgewählt werden.")
        elif self.asop and self.gastgeber_spieler:
            raise ValidationError("Entweder ASOP aktivieren oder einen Spieler auswählen, aber nicht beides.")

    def __str__(self):
        gastgeber_info = self.gastgeber_spieler.name if self.gastgeber_spieler else "ASOP"
        return f"{gastgeber_info}: Event am {self.datum} mit Pot: {self.pot} EUR"

class EventTeilnahme(models.Model):
    spieler = models.ForeignKey(Spieler, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    eventgewinn = models.DecimalField(max_digits=10, decimal_places=2, default=0)

