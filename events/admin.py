from django.contrib import admin

# Register your models here.

from .models import Event, EventParticipant, EventSelection, Bookmaker, Market, MarketSelection, Odds, Participant, ParticipationType, Results, Sport, Venue


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    pass