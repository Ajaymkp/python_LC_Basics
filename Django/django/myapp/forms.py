from django.forms import ModelForm
from .models import *
class Stud_form(ModelForm):
    class Meta:
        model=Student
        fields="__all__"