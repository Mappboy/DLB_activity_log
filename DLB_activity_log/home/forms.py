# Forms stuff goes in here
from models import *
#from django.forms.extras.widgets import SelectDateWidget
from django.forms.models import inlineformset_factory
from django.contrib.admin.widgets import *
# TODO: Create forms for most of our models
# Can we use modelChoice


class CreateDLUIdForm(forms.ModelForm):
    """
    Project id in forms maybe if not in list create new
    """

    class Meta:
        model = DLUId
        fields = ['projectid']


class CreateContactForm(forms.ModelForm):
    """
    Form for adding a new contact
    """

    class Meta:
        model = Client
        fields = ['name', 'email']

class CreateLinkerForm(forms.ModelForm):
    """
    Form for adding a new linkage officer
    """

    class Meta:
        model = Linker
        fields = '__all__'

class CreateDatasetForm(forms.ModelForm):
    """
  Form for creating a new dataset
  """

    class Meta:
        model = Dataset
        fields = '__all__'


class CreateBatchForm(forms.ModelForm):
    """
    Form for creating new data batch
    """

    class Meta:
        model = Batch
        fields = "__all__"
        labels = {'data_received': 'Date Received'}
        widgets = {'data_received': AdminDateWidget()}
        help_texts = {'data_received': 'Data batch received'}
        error_messages = {}

IdFormset = inlineformset_factory(DLUId, Dataset)
ContactFormSet = inlineformset_factory(Client, Dataset)