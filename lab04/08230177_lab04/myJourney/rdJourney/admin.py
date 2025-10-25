from django.contrib import admin
from .models import LearningJourney, AboutMe

@admin.register(LearningJourney)
class LearningJourneyAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'description')
    list_filter = ('date',)
    search_fields = ('title', 'description')

@admin.register(AboutMe)
class AboutMeAdmin(admin.ModelAdmin):
    list_display = ('name', 'email')
    search_fields = ('name', 'bio', 'email')

