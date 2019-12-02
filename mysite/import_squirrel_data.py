import os
import csv

from django.core.management.base import BaseCommand, CommandError
from .models import Squirrel 

class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('args', nargs='*')

    def handle(self, *args,**options):
        csvpath=args[0]
        fields_name = []
        with open (csvpath) as csvfile:
            reader = csv.reader (csvfile)
            header=csvfile.readline().strip().split(',')
            fields_name=[x.replace(' ','_') for x in header]
            for row in reader:
                 obj = squirrel()
                 for i, field in enumerate(row):
                     if field=='true':
                         field=True
                     if field=='false':
                         field=False
                    
                     setattr (obj, fields_name[i], field)

                 obj.save ()
                
