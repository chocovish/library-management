from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User,Book

class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields=['first_name','last_name','username','email','roll','phone','stream']

class BookAddForm(forms.ModelForm):
    class Meta:
        model= Book
        exclude = ['available','borrower']

