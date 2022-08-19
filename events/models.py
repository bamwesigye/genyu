from django.db import models
from django.utils.translation import gettext as _
from django.urls import reverse


# Create your models here.

class Sport(models.Model):
    sport_name = models.CharField(max_length=100)    

    class Meta:
        verbose_name = _("Sport")
        verbose_name_plural = _("Sports")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("eventtype_detail", kwargs={"pk": self.pk})

class Participant(models.Model):
    Participant_name = models.CharField(max_length=255, verbose_name="Team/Individual")
    sport = models.ForeignKey(Sport,on_delete=models.CASCADE)
    notes = models.TextField(_("Notes"), blank=True)
    rating = models.DecimalField(default=0.00, decimal_places=3)

    class Meta:
        verbose_name = _("participant")
        verbose_name_plural = _("participants")

    def __str__(self):
        return self.Participant_name

    def get_absolute_url(self):
        return reverse("participant_detail", kwargs={"pk": self.pk})

class EventParticipant(models.Model):
    event = models.ForeignKey('Event', on_delete=models.CASCADE)
    participant = models.ForeignKey(Participant, on_delete=models.CASCADE)
    notes = models.TextField(_("Notes"), blank=True)
    rating = models.DecimalField(default=0.00, decimal_places=3)

    class Meta:
        verbose_name = _("event participant")
        verbose_name_plural = _("event participants")

    def __str__(self):
        return self.event.event_name + ' ' + self.participant.Participant_name

    def get_absolute_url(self):
        return reverse("eventparticipant_detail", kwargs={"pk": self.pk})
class Event(models.Model):
    event_datetime = models.DateTimeField()
    sport = models.ForeignKey("Event.EventType", verbose_name=_("sport"), on_delete=models.CASCADE)
    event_participant = models.ForeignKey

    

    class Meta:
        verbose_name = _("event")
        verbose_name_plural = _("events")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("events_detail", kwargs={"pk": self.pk})
