from django import forms
from .models import *
  
class UserImageForm(forms.ModelForm):
  
    class Meta:
        model = UploadImage
        fields = '__all__'aditya