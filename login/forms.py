from django import forms
from .models import LoginData

class LoginForm(forms.ModelForm):
    """docstring for ."""
    class Meta:
        model   = LoginData
        exclude = ('reg_no','reg_date')
