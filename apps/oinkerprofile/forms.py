from django import forms

from .models import OinkerProfile

class OinkerprofileForm(forms.ModelForm):
    class Meta:
        model = OinkerProfile
        fields = ('avatar',)