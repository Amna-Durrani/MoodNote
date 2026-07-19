from django.contrib import admin
from .models import WellnessEntry

@admin.register(WellnessEntry)
class WellnessEntryAdmin(admin.ModelAdmin):
    list_display = ('user', 'date', 'sleep_hours', 'bp_systolic', 'bp_diastolic', 'anxiety_level', 'stress_level', 'mood_rating', 'wellness_score', 'gender_identity', 'experienced_discrimination')
    list_filter = ('date', 'body_shivering', 'experienced_discrimination', 'gender_identity')
    search_fields = ('user__email', 'notes', 'discrimination_details')