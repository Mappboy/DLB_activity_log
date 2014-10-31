#! /usr/bin/env python2.7
from django.views.generic import TemplateView

class HomeView(TemplateView):
    template_name = 'home.html'

    def get(self, request, *args, **kwargs):
        context = {
            'some_dynamic_value': 'This text comes from django view!',
        }
        return self.render_to_response(context)
sample_queries = '''
Which linkers have currently open formats or things 

When should we be requesting new datasets

When should we be destroying datasets.

Over view of a dataset

Over view of an organisation

Batches available for each dataset
'''
