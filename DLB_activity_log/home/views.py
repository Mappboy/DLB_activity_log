#! /usr/bin/env python2.7
import django.http
from django.shortcuts import render

from models import Dataset
from .forms import CreateDatasetForm, create_new_datasets
from django.views.generic import *


class HomeView(TemplateView):
    template_name = 'home.html'

    def get(self, request, *args, **kwargs):
        context = {
            'some_dynamic_value': 'This text comes from django view!',
        }
        return self.render_to_response(context)




class Combinedform(FormView):
    template_name = 'form-inline.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {'form': create_new_datasets()})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return django.http.HttpResponseRedirect('/save_dataset/', form)

        return render(request, self.template_name, {'form': form})

class CreateDataset(View):
    """
    Experimenting with view classes
    """
    form_class = CreateDatasetForm
    initial = {'key': 'value'}
    template_name = 'form.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return django.http.HttpResponseRedirect('/save_dataset/', form)

        return render(request, self.template_name, {'form': form})


def save_dataset(request, dataset):
    """
    Save a dataset
    :param request:
    :param dataset:
    :return:
    """
    return django.http.HttpResponse('<h1>' + "YAY, you saved %s " % dataset.clean_fields()['name'] + '</h1>')


#not sure whether to use name or id
def edit_dataset(request, datasetname):
    """
    Edit existing dataset
    :param request:
    :param datasetname:
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
    return django.http.HttpResponse("<h1>Hello Views</h1>")
    
sample_queries = '''
Which linkers have currently open formats or things 

When should we be requesting new datasets

When should we be destroying datasets.

Over view of a dataset

Over view of an organisation

Batches available for each dataset
'''
