from django import forms
from .models import SynthLog

class SynthLogForm(forms.ModelForm):
    class Meta:
        model = SynthLog
        fields = ['log_type', 'date', 'description']
        widgets = {
            'log_type': forms.Select(attrs={
                'class': 'form-control',
            }),
            'date': forms.DateInput(attrs={
                'type': 'date',
                'class': 'form-control',
            }),
            'description': forms.Textarea(attrs={
                'rows': 4,
                'placeholder':  'Describe the service, mod, or accessory...',
                'class': 'form-control',
            }),
        }