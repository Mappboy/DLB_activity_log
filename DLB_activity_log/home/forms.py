# Forms stuff goes in here
from django import forms
from models import *

# TODO: Create forms for most of our models


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
        fields = ['name', 'email']


class CreateDatasetForm(forms.ModelForm):
    """
  Form for creating a new dataset
  """

    class Meta:
        model = Dataset
        fields = ['name',
                  'restricted',
                  'categories',
                  'update_cycle',
                  'contact',
                  'dlb_project_id',
                  'created_by']


class CreateBatch(forms.ModelForm):
    """
    Form for creating new data batch
    """

    class Meta:
        model = Batch
        fields = []