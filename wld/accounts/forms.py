from django import forms
from .models import User,UserData

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email', 'password']
        widgets = {
            'password': forms.PasswordInput(),
        }
class UserDataForm(forms.ModelForm):
    class Meta:
        model = UserData
        fields = ['username', 'key']