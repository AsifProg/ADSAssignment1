from django import forms
from .models import Records  # Change Contact to your model

class ContactForm(forms.ModelForm):
    class Meta:
        model = Records
        fields = ['id' 'fname', 'lname']  # Fields to update
