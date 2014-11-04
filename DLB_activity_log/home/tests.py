#testing script for DLB_log
"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".
Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from DLB_activity_log.home.models import *
from DLB_activity_log.home.forms import *

# TODO: Create test cases for models
class DatasetTestCase(TestCase):
    def setUp(self):
        testset = {'name':'morb',
              'restricted':False,
              'categories':'CI',
              'contact':Client(name='Joe Blogs',email='Joe.Blogs@health.wa.gov.au'),
              'updatecylce':'M',
              'dlbprojectid':DLUId(),
              'overview':"This dataset bleongs to the morbidity HMDS blah blah blah"}
        Dataset.objects.create(testset)

    def test_dataset_name(self):
        """Testing name is recorded correctly"""
        morb = Dataset.objects.get(name='morb')
        self.assertEqual(morb.name,'morb',"Dataset records name")

class TestdatasetForm(TestCase):
    def setUp(self):
        testset = {'name':'morb',
              'restricted':False,
              'categories':'CI',
              'contact':Client(name='Joe Blogs',email='Joe.Blogs@health.wa.gov.au'),
              'updatecycle':'M',
              'dlbprojectid':DLUId(),
              'overview':"This dataset bleongs to the morbidity HMDS blah blah blah"}
    def test_form_valid(self):
        """Testing form for dataset is working correctly"""
        test_dataset_form = CreateDatasetForm(testset)
        self.assertTrue(test_dataset_form.is_valid())
        
    def test_form_isinvalid(self):
        """Testing form is failing correctly"""
        testset['nextupdate'] = None
        test_dataset_form = CreateDatasetForm(testset)
        self.assertFalse(test_dataset_form.is_valid())
        errors = test_dataset_form.errors.as_data()
        # TODO: check is InValidField  
        
class PersonTestCase(TestCase):
    pass

class UpdateTestCase(TestCase):
    pass
