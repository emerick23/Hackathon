from django.forms import ModelForm 
from .models import Outcome, Job

class OutcomeForm(ModelForm):
    class Meta:
        model = Outcome
        fields = ['note']

class StageForm(ModelForm):
    class Meta:
        model = Job
        fields = ['stage']

class PrioritizeForm(ModelForm):
    class Meta:
        model = Job
        fields = ['prioritized']