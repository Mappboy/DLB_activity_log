#! /usr/bin/env python2.7
from django.views.generic import TemplateView
from django.http import HttpResponse
from models import Dataset

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
    
sample_queries = '''
Which linkers have currently open formats or things 

When should we be requesting new datasets

When should we be destroying datasets.

Over view of a dataset

Over view of an organisation

Batches available for each dataset
'''
