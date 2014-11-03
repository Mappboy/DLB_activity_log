#! /usr/bin/env python2.7
from django.views.generic import TemplateView, View
from django.http import HttpResponse
from django.shortcuts import render

from models import Dataset
from .forms import CreateDatasetForm

class HomeView(TemplateView):
    template_name = 'home.html'

    def get(self, request, *args, **kwargs):
        context = {
            'some_dynamic_value': 'This text comes from django view!',
        }
        return self.render_to_response(context)

def create_dataset(request):
    """
    Create a new dataset view
    """
    return render_to_response('create_dataset.html')

class CreateDataset(View):
    """
    Experimenting with view classes
    """
    form_class = CreateDatasetForm
    initial = {'key': 'value'}
    template_name = 'create_dataset.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            # <process form cleaned data>
            return HttpResponseRedirect('/success/')

        return render(request, self.template_name, {'form': form})

#not sure whether to use name or id
def edit_dataset(request,datasetname):
    """
    Edit existing dataset
    """
    try:
        ds_to_edit = Dataset.objects.get(name=datasetname)
    except Dataset.DoesNotExist:
        raise Http404
    return render_to_response('edit_dataset.html')
    
def display_dataset(request,datasetname):
    """
    Return a complete overview for each dataset
    """
    return render_to_response('dataset_overview.html')

def testview(request):
    return HttpResponse("<h1>Hello Views</h1>")
    
sample_queries = '''
Which linkers have currently open formats or things 

When should we be requesting new datasets

When should we be destroying datasets.

Over view of a dataset

Over view of an organisation

Batches available for each dataset
'''
