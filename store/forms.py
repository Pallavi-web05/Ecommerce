from django import forms
from .models import*

class productform(forms.ModelForm):
    class Meta:
     model = Product
     fields = ['name','price','category','description','image']