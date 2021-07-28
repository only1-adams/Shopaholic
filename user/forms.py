from django import forms
# from django.forms import ModelForm
# from django.forms import TextInput, EmailInput, FileInput, Select
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# from .models import UserProfile

class RegistrationForm(UserCreationForm):
    username = forms.CharField(max_length=30, help_text='username')
    first_name = forms.CharField(max_length=50, help_text='first_name')
    last_name = forms.CharField(max_length=50, help_text='last_name')
    email = forms.EmailField(max_length=50, help_text='email')
    date= forms.DateField(help_text='date')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email',  'password1', 'password2', 'date',)

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
            return user