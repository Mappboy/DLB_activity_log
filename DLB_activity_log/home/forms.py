#Forms stuff goes in here
from django import forms
from models import *
from django.forms.models import inlineformset_factory

# TODO: Create forms for most of our models

def create_new_datasets():
  return inlineformset_factory(CreateDatasetForm,CreateContact,CreateDLUID)

class CreateDLUID(forms.ModelForm):
  """
  Project id in forms maybe if not in list create new
  """
  class Meta:
  model = DLUId
  fields = ['projectid']
  
  
class CreateContact(forms.ModelForm):
  """
  Form for adding a new contact
  """
  class Meta:
  model = Client
  fields = ['name','email']
  
  
class CreateDatasetForm(forms.ModelForm):
  """
  Form for creating a new dataset
  """
  class Meta:
    model = Dataset
    fields = ['name',
              'restricted',
              'categories',
              'contact',
              'nextupdate',
              'dlbprojectid']
    

class EditDatasetForm(forms.Form):
  """
  Form for editing a new dataset
  """
  class Meta:
    model = Dataset
    fields = ['name',
              'restricted',
              'categories',
              'contact',
              'nextupdate',
              'dlbprojectid']
