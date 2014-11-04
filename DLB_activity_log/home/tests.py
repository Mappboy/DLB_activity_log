# testing script for DLB_log
"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".
Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from DLB_activity_log.home.forms import *

# TODO: Create test cases for models
class DatasetTestCase(TestCase):
    def setUp(self):
        joebloggs = Client(name='Joe Blogs', email='Joe.Blogs@health.wa.gov.au')
        joebloggs.save()
        morbid = DLUId(projectid="219114.11")
        morbid.save()
        testset = dict(name='morb', restricted=False, categories='CI', contact=joebloggs, updatecycle='M',
                       dlbprojectid=morbid, overview="This dataset belongs to the morbidity HMDS blah blah blah")
        Dataset.objects.create(**testset)

    def test_dataset_name(self):
        """Testing name is recorded correctly"""
        morb = Dataset.objects.get(name='morb')
        self.assertEqual(morb.name, 'morb', "Dataset records name")


class TestdatasetForm(TestCase):
    def setUp(self):
        """
        Testing for CreateDatasetForm
        """
        joebloggs = Client(name='Joe Blogs', email='Joe.Blogs@health.wa.gov.au')
        joebloggs.save()
        pid = DLUId(projectid="219114.11")
        pid.save()
        self.testset = dict(name='morb', restricted=False, categories='CI',
                            contact=joebloggs.id, updatecycle='M',
                            dlbprojectid=pid.id,
                            overview="This dataset belongs to the morbidity HMDS blah blah blah")
        self.test_dataset_form = CreateDatasetForm(data=self.testset)

    def test_form_valid(self):
        """Testing form for dataset is working correctly"""
        self.assertTrue(self.test_dataset_form.is_valid())

    def test_form_isinvalid(self):
        """Testing form is failing correctly"""
        self.testset['updatecycle'] = None
        test_dataset_form = CreateDatasetForm(data=self.testset)
        self.assertFalse(self.test_dataset_form.is_valid())
        errors = self.test_dataset_form.errors.as_data()
        # TODO: check is InValidField  


class PersonTestCase(TestCase):
    pass


class UpdateTestCase(TestCase):
    pass
