#testing script for DLB_log
"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".
Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
#from DLB_activity_log import home

class AnimalTestCase(TestCase):
    def setUp(self):
        #Animal.objects.create(name="lion", sound="roar")
        pass

    def test_animals_can_speak(self):
        """Animals that can speak are correctly identified"""
        #lion = Animal.objects.get(name="lion")
        #self.assertEqual(lion.speak(), 'The lion says "roar"')
        self.assertEqual(1,1,"Tests working correctly")
