from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator


class WellnessEntry(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='wellness_entries')
    date = models.DateField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    # General
    sleep_hours = models.DecimalField(max_digits=4, decimal_places=1, validators=[MinValueValidator(0), MaxValueValidator(24)])
    sleep_quality = models.PositiveSmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)])
    bp_systolic = models.PositiveSmallIntegerField(validators=[MinValueValidator(70), MaxValueValidator(200)])
    bp_diastolic = models.PositiveSmallIntegerField(validators=[MinValueValidator(40), MaxValueValidator(130)])
    anxiety_level = models.PositiveSmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)])
    stress_level = models.PositiveSmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)])
    fatigue_level = models.PositiveSmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)])
    mood_rating = models.PositiveSmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)])
    body_shivering = models.BooleanField(default=False)
    shivering_intensity = models.PositiveSmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)], blank=True, null=True)
    
    # Gender
    GENDER_CHOICES = [('', '--'), ('male', 'Male'), ('female', 'Female'), ('non_binary', 'Non-binary'), ('transgender_male', 'Transgender Male'), ('transgender_female', 'Transgender Female'), ('prefer_not_to_say', 'Prefer not to say'), ('other', 'Other')]
    gender_identity = models.CharField(max_length=20, choices=GENDER_CHOICES, blank=True)
    irritability_level = models.PositiveSmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)], blank=True, null=True)
    appetite_level = models.PositiveSmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)], blank=True, null=True)
    anger_attacks = models.PositiveSmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)], blank=True, null=True)
    loneliness_level = models.PositiveSmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)], blank=True, null=True)
    experienced_discrimination = models.BooleanField(default=False)
    discrimination_details = models.TextField(blank=True)
    
    notes = models.TextField(blank=True)
    
    class Meta:
        ordering = ['-date']
        unique_together = ['user', 'date']
    
    @property
    def bp_status(self):
        if self.bp_systolic < 120 and self.bp_diastolic < 80: return "Normal"
        elif 120 <= self.bp_systolic < 130 and self.bp_diastolic < 80: return "Elevated"
        elif 130 <= self.bp_systolic < 140 or 80 <= self.bp_diastolic < 90: return "High Stage 1"
        else: return "High Stage 2"
    
    @property
    def wellness_score(self):
        return min(round((self.sleep_hours/8)*20 + self.sleep_quality*2 + (11-self.anxiety_level)*2 + (11-self.stress_level)*2 + (11-self.fatigue_level)*2), 100)
    
    @property
    def gender_wellness_score(self):
        if not self.irritability_level: return None
        total = (11-self.irritability_level)*2.5 + self.appetite_level*2.5 + (11-self.anger_attacks)*2.5 + (11-self.loneliness_level)*2.5
        if self.experienced_discrimination: total -= 10
        return max(min(round(total), 100), 0)