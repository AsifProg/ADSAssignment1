from django import forms
from .models import Records  # Change Contact to your model

class RecordForm(forms.ModelForm):
    class Meta:
        model = Records
        fields = ['record_id' ,'first_name', 'last_name']  # Fields to update
