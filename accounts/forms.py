from django import forms


class UserLoginForm(forms.Form):
    """Form for users login"""

    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    
    