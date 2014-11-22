#! /usr/bin/env python2.7
import django.http
from django.shortcuts import render_to_response
from .forms import *
from django.views.generic import *


class HomeView(TemplateView):
    template_name = 'home.html'

    def get(self, request, *args, **kwargs):
        context = {
            'some_dynamic_value': 'This text comes from django view!',
        }
        return self.render_to_response(context)

class DatasetList(ListView):
    model = Dataset

class NewDataset(FormView):
    """
    Experimenting with view classes
    """
    form_class = CreateDatasetForm
    template_name = 'createdataset.html'
    success_url = '/success/'


class CreateDataset(CreateView):
    """
    Experimenting with view classes
    """
    form_class = CreateDatasetForm
    model = Dataset
    template_name = 'createdataset.html'
    success_url = 'success/'

    def get(self, request, *args, **kwargs):
        """
        Handles GET requests and instantiates blank versions of the form
        and its inline formsets.
        """
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        client_form = ContactFormSet()
        dluid_form = IDFormSet()
        return self.render_to_response(
            self.get_context_data(form=form,
                                  client_form=client_form,
                                  dluid_form=dluid_form))

    def post(self, request, *args, **kwargs):
        """
        Handles POST requests, instantiating a form instance and its inline
        formsets with the passed POST variables and then checking them for
        validity.
        """
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        client_form = ContactFormSet(self.request.POST)
        dluid_form = IDFormSet(self.request.POST)
        if (form.is_valid() and client_form.is_valid() and
                dluid_form.is_valid()):
            return self.form_valid(form, client_form, dluid_form)
        else:
            return self.form_invalid(form, client_form, dluid_form)

    def form_valid(self, form, client_form, dluid_form):
        """
        Called if all forms are valid. Creates a Recipe instance along with
        associated Ingredients and Instructions and then redirects to a
        success page.
        """
        self.object = form.save()
        client_form.instance = self.object
        client_form.save()
        dluid_form.instance = self.object
        dluid_form.save()
        return HttpResponseRedirect(self.get_success_url())

    def form_invalid(self, form, client_form, dluid_form):
        """
        Called if a form is invalid. Re-renders the context data with the
        data-filled forms and errors.
        """
        return self.render_to_response(
            self.get_context_data(form=form,
                                  client_form=client_form,
                                  dluid_form=dluid_form))


class DelDataset(DeleteView):
    """
    Delete a dataset
    """



# not sure whether to use name or id
class UpdateDataset(UpdateView):
    """
    Edit existing dataset
    """



def display_dataset(request, datasetname):
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
