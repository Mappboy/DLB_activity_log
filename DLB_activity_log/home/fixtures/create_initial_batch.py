#!/usr/bin/env python2.7
#Script for creating a proper working initial data
#NOTE: going to need customDataset for midwives 
#NOTE: This started out extremely pretty and just got a little hacky.
#Need not run spectacularly
#Cameron Poole 25/11/14

import csv
import json
import datetime
from itertools import izip_longest,izip
from dateutil.relativedelta import relativedelta
import pprint


jsonfile = "initial_data.json"

users = {"cameronp":["cam","cameron"],
        "mikha":["mikha","mikhalina"],
        "helenw":["helen"],
        "clintonp":["clinton"],
        "jennyc":["jenny"],
        "shaneu":["shane"],
        "margaretw":["margaret"],
        "bhavalc":["bhaval"]
        }

init_data = json.load(open(jsonfile,'r'))

#primary key ids
datasetids=2
personid=2
contactid=2

datasetfields=["name","update_cycle",
                "categories","dlb_project_id",
                "created_by","overview","contact"
                ]

batchfields=["datasetid",
    "batch_type",
    "data_format",
    "media",
    "data_coverage_start",
    "data_coverage_end",
    "filepath",
    "data_recieved",
    "created_by",
    "records_in_new",
    "records_in_cor",
    "records_loaded_new",
    "records_loaded_cor",
    "records_skipped",
    "format_changed",
    "date_to_destroy",
    "new_profile",
    "trac_ticket",
    "person_from",
    ]

midbatch = ["records_deleted","diff_count"] + batchfields
midbatch.insert(5,midbatch.pop(0))
midbatch.insert(5,midbatch.pop(0))


idlookup = {'home.Dataset':{},
                'home.Linker':{},
                'home.Batch':{},
                'home.Client':{}}

for js in init_data:
    try:
        idlookup[js['model']].update({js['fields']['name']:js['pk']})
    except:
        idlookup[js['model']].update({js['fields']['username']:js['pk']})

months = ['Jan',
 'Feb',
 'Mar',
 'Apr',
 'May',
 'Jun',
 'Jul',
 'Aug',
 'Sep',
 'Oct',
 'Nov',
 'Dec'
 ]

batchfile = "2013_core-batch.csv"
myreader = csv.reader(open(batchfile,'r'))

date = datetime.date.today()

#need file path mapping for datasets
filepaths =  {'Morbidity': "/raw_data/morbidity/{year}/{month}",
  'Births': "/raw_data/birth/{year}/{month}",
  'Deaths': "/raw_data/death/{year}/{month}",
  'Marriages':"/raw_data/marriage/{year}/{month}",
  'Cancer': "/raw_data/cancers/{year}/{month}",
  'Midwives': "/raw_data/midwives/{year}/{month}",
  'Electoral Roll': "/raw_data/elect/{year}/{month}"}


def default(obj):
    """Default JSON serializer. Need to serialise date time objects *sigh*"""
    import calendar, datetime

    if isinstance(obj, datetime.datetime):
        if obj.utcoffset() is not None:
            obj = obj - obj.utcoffset()
    millis = int(
        calendar.timegm(obj.timetuple()) * 1000 +
        obj.microsecond / 1000
    )
    return millis


def fixnums(line,months,year,type,dataset,all=True):
    """
    Return a list of datetime objects with appropriate records for a given year
    """
    records = line[1:13]
    cleaned_data = []
    y = str(year)
    getstart = {'M':relativedelta(months=-1),
            'Q':relativedelta(months=-3),
            'B':relativedelta(months=-6),
            'Y':relativedelta(years=-1),
            'O':relativedelta(),
            'U':relativedelta()}
    for number,mon in zip(records,months):
        if number == '' or number == 'n/a':
            continue
        if '(' in number:
            number = number[:number.index('(')]
        record_count = int(number.translate(None,",*"))
        end_date = datetime.datetime.strptime(y+mon+"01","%Y%b%d")
        start_date = end_date+getstart[type]
        if dataset:
            cormon = "0" + str(end_date.month) if end_date.month < 10 else str(end_date.month)
            fp = filepaths[dataset].format(year=end_date.year,month=cormon)
        if not all:
            cleaned_data.append(record_count)
        else:
            cleaned_data.append([start_date,end_date,record_count,fp])
    return cleaned_data


date_formats = ["%d/%m/%Y","%d/%m/%y"]
batch_stuff = []
new_records, new_loaded,cor_records = [],[],[] 
cor_loaded,creators,load_dates = [],[],[]
records_del, record_diff = [],[]
start_dates,end_dates,fps = [],[],[]
batchprimkey=1

for row in myreader:
    #Skip first row
    month = 1
    day = 1
    categories = 'CI'
    update_cycle = 'M'
    batch_type = 'n'
    data_format = 'd'
    format_changed = False
    new_dataset = False
    media = 'soft'
    restricted = False
    headcol = row[0]
    if myreader.line_num == 2:
        year = headcol 
    if headcol.endswith('*') or headcol == 'Midwives':
        #add new datasets and primary keys
        dataset = unicode(headcol.rstrip('*'))
        if dataset not in idlookup['home.Dataset']:
            idlookup['home.Dataset'].update({dataset:datasetids})
            update_cycle = 'B' if dataset == 'Electoral Roll' else 'M'
            new_batch_fields = dict([ field for field in\
                    izip_longest(datasetfields,[dataset,update_cycle,categories]) ])
            init_data.append(json.loads(json.dumps({
                        "model":'home.Dataset',
                        "pk":datasetids,
                        "fields":new_batch_fields
                        }
                        )))
            datasetids+=1
        continue

        
    #TODO create a dictionary of batch variables
    if 'records in' in headcol.lower() and not "[c]" in headcol:
        start_dates,end_dates,new_records,fps = zip(*fixnums(row,months,year,update_cycle,dataset))
    if 'records loaded' in headcol.lower() and not "[c]" in headcol:
        new_loaded = fixnums(row,months,year,update_cycle,False,False)
    if 'records in [c]' in headcol.lower() or 'records in c' in headcol.lower():
        cor_records = fixnums(row,months,year,update_cycle,False,False)
    if 'records loaded [c]' in headcol.lower() or 'records loaded c' in headcol.lower():
        cor_loaded = fixnums(row,months,year,update_cycle,False,False)
    if 'record count diff' in headcol.lower():
        record_diff = fixnums(row,months,year,update_cycle,False,False)
    if 'record deleted' in headcol.lower():
        records_del = fixnums(row,months,year,update_cycle,False,False)
    if headcol.lower() == 'date loaded':
        #lazy, butttt what am I superman.
        load_dates = []
        for dateval in row[1:13]:
            for d in date_formats:
                try:
                    load_dates.append(datetime.datetime.strptime(dateval,d))
                    break
                except:
                    continue
    if headcol.lower() == 'sign-off':
        creators = []
        for name in row[1:13]:
            for key,values in users.iteritems():
                if name != '' and name.lower().split()[0] in values:
                    creators.append(key)
                    break
        new_dataset = True

    if new_dataset and dataset != u'Midwives':
        prim_key=0
        for prim_key,batch_zipped in enumerate(izip_longest(start_dates,
                                            end_dates,
                                            fps,
                                            load_dates,
                                            creators,
                                            new_records,
                                            new_loaded,
                                            cor_records,
                                            cor_loaded)):
            init_data.append(json.loads(json.dumps({"pk":prim_key+batchprimkey,
                                    "model":"model.Batch",
                "fields":zip(batchfields,[idlookup['home.Dataset'][dataset],
                    batch_type,data_format,media]+ list(batch_zipped))},default=default
                )))
        batchprimkey+=prim_key

    elif new_dataset and dataset == u'Midwives':
        for  prim_key,batch_zipped in enumerate(izip_longest(records_del,
                                            record_diff,
                                            start_dates,
                                            end_dates,
                                            fps,
                                            load_dates,
                                            creators,
                                            new_records,
                                            new_loaded,
                                            cor_records,
                                            cor_loaded)):
            init_data.append(json.loads(json.dumps({"pk":prim_key+batchprimkey,
                                    "model":"model.Batch",
                "fields":zip(midbatch,[idlookup['home.Dataset'][dataset],
                    batch_type,data_format,media]+ list(batch_zipped))},default=default
                )))
        batchprimkey+=prim_key
