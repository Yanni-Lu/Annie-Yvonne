import os
import csv

from django.core.management.base import BaseCommand, CommandError
#import sys
#sys.path.append('../../')
from mysite.models import Squirrel 

class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('args', nargs='*')

    def handle(self, *args,**options):
        filepath=args[0]
        fields_name = []
        with open (filepath) as csvfile:
            content = csv.reader (csvfile)
            totalname = csvfile.readline().strip().split(',')
            fieldname = [i.replace(' ','_').replace('/','_') for i in totalname]
            for line in content:
                 data = Squirrel()
                 for x, field in enumerate(line):
                     if field=='true':
                         field=True
                     if field=='false':
                         field=False
                    
                     setattr (data, fieldname[x], field)

                 data.save ()
