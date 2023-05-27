from django import forms
from .models import PlanAffaireCreation


class PlanAffaireCreationForm(forms.ModelForm):
    class Meta:
        model = PlanAffaireCreation
        exclude = ['id']
