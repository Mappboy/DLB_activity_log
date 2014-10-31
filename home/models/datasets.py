# Author:Cameron Poole
# Date  : 31/10/14
# Data models for dlb data logger so far
# Hopefully get something implemented reasonable quickly
# TODO: CREATE DLU_ID class

from django.db import models
from people import Client,Linker


class Update():
    pass


class DLUId(models.Model):
    '''
    Information about a particular dlu id
    '''
    projectid = models.CharField()


class Dataset(models.Model):
    """
    Stores data about each dataset
    """
    TYPE = (('CI','Core Infrastructure'),
            ('NI','Non-Core Infrastructure'),
            ('RN','Recurring'),
            ('A','Adhoc'),
            ('O','Other'))
    name = models.CharField(max_length=50)
    restricted = models.BooleanField()
    categories = models.CharField(max_length=1,choices=TYPE)
    contact = models.ManyToManyField(Client)
    nextupdate = models.ManyToOne(Update)
    dlbprojectid = models.ManyToOne(DLUId)

class Batch(models.Model):
    '''
    Stores information for a new batch for each data set
    '''
    FORMATS = ('del',
                'csv',
                'fixed',
                'other')
    #I included update although maybe I shouldn't
    TYPE = ('New',
            'Correction',
            'Refresh',
            'Update')
    datasetid = models.ForeignKey('Dataset')
    data_recieved = models.DateField()
    #capture date start and end
    data_coverage_start = models.DateField()
    data_coverage_end = models.DateField()
    data_format = models.CharField(max_length=5,choice=FORMATS)
    format_changed = models.BooleanField()
    #Store hard or soft media
    media = models.Charfield()
    person_from = models.ManyToManyField(Client)
    person_recieved = models.ManyToManyField(Linker)
    #Path on linkage side usually /raw_data/
    filepath = models.CharField()
    #Only necessary for adhoc
    date_to_destroy = models.DateField()
    # for now check if load profile is needed in future email dev create trac ticket
    new_profile = models.BooleanField()
    # Related trac ticket number
    trac_ticket = models.IntegerField()
    # Record number of records in and loaded
    recordsin = models.IntegerField()
    recordsloaded = models.IntegerField()
    
    def createdestructiondate(self):
        "Create a destroy date we can use some info to autogenerate this "
        #import datetime
        #if "adhoc" or "non-core":
        #date_to_destroy = datetime.now() + "5 YEARS"
        #Reminder(date,destructioninfo)
        #set a reminder
        pass


class Stage(models.Model):
    '''
    Stores information for each stage of a batch
    '''
    STAGE = ('EV','Evaluating',
            'CL', 'Cleaning',
            'EX','Exporting',
            'LI','Linkage')
    batchid = models.ForeignKey('Batch')
    startdate = models.DateField()
    starttime = models.TimeField() #Optional ?? 
    enddate = models.DateField()
    endtime = models.TimeField() #Optional ??'
    controller = models.OneToOne(Linker)
class HardMedia(models.Model):
    '''
    Capture if it came in on a flash drive , or disk
    '''
    #location where it is stored
    pass

class SoftMedia(models.Model):
    '''
    Want to capture if it came through myft, suffex,email etc 
    '''
    pass

class Destruction(models.Model):
    '''
    Store information about what to destroy
    Links, Data, Media, Date etc...
    '''
    pass
