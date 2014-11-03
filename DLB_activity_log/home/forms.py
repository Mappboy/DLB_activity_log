#Forms stuff goes in here
from django import forms
from models import *

class CreateDatasetForm(forms.ModelForm):
  """
  Form for creating a new dataset
  """
  class Meta:
    model = Dataset
    fields = ['name']
    

class EditDatasetForm(forms.Form):
  """
  Form for editing a new dataset
  """
  class Meta:
    model = Dataset
    fields = ['name']
