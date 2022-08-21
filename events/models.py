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


class Venue(models.Model):
    venue_name = models.CharField(max_length=100)    

    class Meta:
        verbose_name = _("Venue")
        verbose_name_plural = _("Venues")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Venue_detail", kwargs={"pk": self.pk})


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


class Event(models.Model):
    event_datetime = models.DateTimeField()
    sport = models.ForeignKey(Sport, verbose_name=_("sport"), on_delete=models.CASCADE)
    venue = models.ForeignKey("Event.Venue", verbose_name=_("venue"), on_delete=models.CASCADE)
    

    class Meta:
        verbose_name = _("event")
        verbose_name_plural = _("events")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("events_detail", kwargs={"pk": self.pk})


class ParticipationType(models.Model):

    name = models.CharField(max_length=5)

    class Meta:
        verbose_name = _("participationType")
        verbose_name_plural = _("ParticipationType")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("participation_type_detail", kwargs={"pk": self.pk})


class EventParticipant(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    participant = models.ForeignKey(Participant, on_delete=models.CASCADE)
    participation_type =models.ForeignKey(Participant, on_delete=models.CASCADE)
    

    class Meta:
        verbose_name = _("event participant")
        verbose_name_plural = _("event participants")

    def __str__(self):
        return self.event.event_name + ' ' + self.participant.Participant_name + ' ' + self.participation_type.name

    def get_absolute_url(self):
        return reverse("event_participant_detail", kwargs={"pk": self.pk})


class Market(models.Model):

    name = models.CharField(max_length=255)
    code = models.CharField(max_length=255)
    Sport = models.ForeignKey(Sport, on_delete=models.CASCADE)

    class Meta:
        verbose_name = _("market")
        verbose_name_plural = _("markets")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("market_detail", kwargs={"pk": self.pk})


class MarketSelection(models.Model):

    market_selection_code = models.CharField(unique=True, max_length=255)
    name = models.CharField(max_length=255)
    market = models.ForeignKey(Market, on_delete=models.CASCADE)

    class Meta:
        verbose_name = _("market selection")
        verbose_name_plural = _("market selections")

    def __str__(self):
        return self.market_selection_code + ' ' + self.name

    def get_absolute_url(self):
        return reverse("market_selection_detail", kwargs={"pk": self.pk})

class Bookmaker(models.Model):

    bookmaker = models.CharField(max_length=255)
    notes = models.TextField(blank=True)

    class Meta:
        verbose_name = _("Bookmaker")
        verbose_name_plural = _("Bookmakers")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Bookmaker_detail", kwargs={"pk": self.pk})

class Results(models.Model):
    result = models.CharField(max_length=50)
    result_color = models.CharField(max_length=50)


class EventSelection(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    selection = models.ForeignKey(MarketSelection, on_delete=models.CASCADE)
    result = models.ForeignKey(Results, )
    

    class Meta:
        verbose_name = _("Event Selection")
        verbose_name_plural = _("Event Selections")

    def __str__(self):
        return self.event + ' '+ self.selection

    def get_absolute_url(self):
        return reverse("event_selection_detail", kwargs={"pk": self.pk})


class Odds(models.Model):

    eventselection = models.ForeignKey(EventSelection,on_delete=models.CASCADE)
    odds_time = models.DateTimeField(auto_now_add=True, auto_now=True)
    odd = models.DecimalField(decimal_places=3)

    class Meta:
        verbose_name = _("odds")
        verbose_name_plural = _("odds")

    def __str__(self):
        return self.odds

    def get_absolute_url(self):
        return reverse("odds_detail", kwargs={"pk": self.pk})


