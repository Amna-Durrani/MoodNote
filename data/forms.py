from django import forms
from django.core.validators import MinValueValidator, MaxValueValidator
from .models import WellnessEntry


class WellnessEntryForm(forms.ModelForm):
    sleep_hours = forms.DecimalField(max_digits=4, decimal_places=1, validators=[MinValueValidator(0), MaxValueValidator(24)], widget=forms.NumberInput(attrs={'class':'form-control','placeholder':'e.g., 7.5','step':'0.5'}), label='Hours Slept')
    sleep_quality = forms.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)], widget=forms.NumberInput(attrs={'class':'form-control','placeholder':'1-10','min':1,'max':10}), label='Sleep Quality', help_text='1=Terrible, 10=Excellent')
    bp_systolic = forms.IntegerField(validators=[MinValueValidator(70), MaxValueValidator(200)], widget=forms.NumberInput(attrs={'class':'form-control','placeholder':'e.g., 120'}), label='BP Systolic')
    bp_diastolic = forms.IntegerField(validators=[MinValueValidator(40), MaxValueValidator(130)], widget=forms.NumberInput(attrs={'class':'form-control','placeholder':'e.g., 80'}), label='BP Diastolic')
    anxiety_level = forms.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)], widget=forms.NumberInput(attrs={'class':'form-control','placeholder':'1-10','min':1,'max':10}), label='Anxiety', help_text='1=None, 10=Severe')
    stress_level = forms.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)], widget=forms.NumberInput(attrs={'class':'form-control','placeholder':'1-10','min':1,'max':10}), label='Stress', help_text='1=None, 10=Extreme')
    fatigue_level = forms.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)], widget=forms.NumberInput(attrs={'class':'form-control','placeholder':'1-10','min':1,'max':10}), label='Fatigue', help_text='1=Energetic, 10=Exhausted')
    mood_rating = forms.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)], widget=forms.NumberInput(attrs={'class':'form-control','placeholder':'1-10','min':1,'max':10}), label='Mood', help_text='1=Very Low, 10=Excellent')
    body_shivering = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'class':'form-check-input'}), label='Body Shivering?')
    shivering_intensity = forms.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)], required=False, widget=forms.NumberInput(attrs={'class':'form-control','placeholder':'1-10'}), label='Shivering Intensity')
    
    gender_identity = forms.ChoiceField(choices=WellnessEntry.GENDER_CHOICES, required=False, widget=forms.Select(attrs={'class':'form-control'}), label='Gender Identity (Optional)')
    irritability_level = forms.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)], required=False, widget=forms.NumberInput(attrs={'class':'form-control','placeholder':'1-10'}), label='Irritability', help_text='1=Calm, 10=Extremely irritable')
    appetite_level = forms.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)], required=False, widget=forms.NumberInput(attrs={'class':'form-control','placeholder':'1-10'}), label='Appetite', help_text='1=No appetite, 10=Eating well')
    anger_attacks = forms.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)], required=False, widget=forms.NumberInput(attrs={'class':'form-control','placeholder':'1-10'}), label='Anger Attacks', help_text='1=None, 10=Frequent')
    loneliness_level = forms.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)], required=False, widget=forms.NumberInput(attrs={'class':'form-control','placeholder':'1-10'}), label='Loneliness', help_text='1=Not lonely, 10=Extremely lonely')
    experienced_discrimination = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'class':'form-check-input'}), label='Gender-based discrimination?')
    discrimination_details = forms.CharField(required=False, widget=forms.Textarea(attrs={'class':'form-control','rows':2}), label='Details (Optional)')
    
    notes = forms.CharField(required=False, widget=forms.Textarea(attrs={'class':'form-control','rows':2}), label='Notes')
    
    class Meta:
        model = WellnessEntry
        fields = ['sleep_hours','sleep_quality','bp_systolic','bp_diastolic','anxiety_level','stress_level','fatigue_level','mood_rating','body_shivering','shivering_intensity','gender_identity','irritability_level','appetite_level','anger_attacks','loneliness_level','experienced_discrimination','discrimination_details','notes']