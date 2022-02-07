from django.forms import forms, models, ModelForm

from .models import personaldetails
from app1 import models
from .models import personaldetails
from django import forms


class personalform(forms.ModelForm):
    class Meta:
        model = personaldetails
        fields = ['name', 'dept', 'age']
