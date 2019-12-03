import os
import csv

from django.core.management.base import BaseCommand, CommandError
from mysite.models import Squirrel

class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('args', nargs='*')

    def handle(self, *args,**options):
        csvpath = args[0]
        with open(csvpath,'w') as output:
            data = Squirrel.objects.all()
            header = [['X','Y','Unique Squirrel ID','Hectare','Shift','Date','Hectare Squirrel Number','Age','Primary Fur Color','Highlight Fur Color','Combination of Primary and Highlight Color','Color notes','Location','Above Ground Sighter Measurement','Specific Location','Running','Chasing','Climbing','Eating','Foraging','Other Activities','Kuks','Quaas','Moans','Tail flags','Tail twitches','Approaches','Indifferent','Runs from','Other Interactions','Lat/Long','Zip Codes','Community Districts','Borough Boundaries','City Council Districts','Police Precincts']]
            totallen = len(data)
            print(data[0])
            print(data[totallen-1])

            print(totallen)
            output.write(data)
            output.close()
