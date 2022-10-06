from django import forms
from .models import ApiModel
  
  
# creating a form
class GeeksForm(forms.ModelForm):
  
    # create meta class
    class Meta:
        # specify model to be used
        model = ApiModel
  
        # specify fields to be used
        fields = [
            "title",
            "description",
        ]