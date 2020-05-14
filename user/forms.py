from ckeditor.widgets import CKEditorWidget
from django import forms
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User
from django.forms import TextInput, FileInput, Select , EmailInput

from home.models import UserProfile
from product.models import Category
from property.models import Properties


class UserUpdateForm(UserChangeForm):
    class Meta:
        model= User
        fields = ('username', 'email', 'first_name', 'last_name')
        widgets = {
            'username' : TextInput(attrs={'class': 'form-control', 'placeholder': 'username'}),
            'email': EmailInput(attrs={'class': 'form-control', 'placeholder': 'email'}),
            'first_name': TextInput(attrs={'class': 'form-control', 'placeholder': 'first_name'}),
            'last_name': TextInput(attrs={'class': 'form-control', 'placeholder': 'last_name'}),
        }

CITY = [
    ('Istanbul', 'Istanbul'),
    ('Ankara', 'Ankara'),
    ('Izmir', 'Izmir'),
    ('Mugla', 'Mugla'),
    ('Aydin', 'Aydin'),
]

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('phone', 'address', 'city', 'country', 'image')
        widgets = {
            'phone': TextInput(attrs={'class': 'form-control', 'placeholder': 'phone'}),
            'address': TextInput(attrs={'class': 'form-control', 'placeholder': 'address'}),
            'city': Select(attrs={'class': 'form-control', 'placeholder': 'city'}, choices=CITY),
            'country': TextInput(attrs={'class': 'form-control', 'placeholder': 'country'}),
            'image': FileInput(attrs={'class': 'form-control', 'placeholder': 'image'}),
        }

class PropertyUpdateForm(forms.ModelForm):
    class Meta:
        model = Properties
        fields = ('category', 'title', 'keywords', 'description', 'image', 'price', 'address', 'room', 'year', 'sqm', 'detail')
        widgets = {
            'category': Select(attrs={'class': 'form-control', 'placeholder': 'category'},),
            'title': TextInput(attrs={'class': 'form-control', 'placeholder': 'title'}),
            'keywords': TextInput(attrs={'class': 'form-control', 'placeholder': 'keywords'}),
            'description': TextInput(attrs={'class': 'form-control', 'placeholder': 'description'}),
            'image': FileInput(attrs={'class': 'form-control', 'placeholder': 'image'}),
            'price': TextInput(attrs={'class': 'form-control', 'placeholder': 'country'}),
            'address': TextInput(attrs={'class': 'form-control', 'placeholder': 'address'}),
            'room': TextInput(attrs={'class': 'form-control', 'placeholder': 'room'}),
            'year': TextInput(attrs={'class': 'form-control', 'placeholder': 'year'}),
            'sqm': TextInput(attrs={'class': 'form-control', 'placeholder': 'sqm'}),
            'detail': CKEditorWidget(),

        }