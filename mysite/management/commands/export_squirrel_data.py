import os
import csv

from django.core.management.base import BaseCommand, CommandError
from mysite.models import Squirrel

class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('csvfile',type=str)

    def handle(self, *args,**options):
        csvpath = options['csvfile']
        squirrels = Squirrel.objects.all()
        with open(csvpath,'w') as csvfile:
            output = csv.writer(csvfile)
            output.writerow(['X','Y','Unique Squirrel ID','Shift','Date','Age','Primary Fur Color','Location','Specific Location','Running','Chasing','Climbing','Eating','Foraging','Other Activities','Kuks','Quaas','Moans','Tail flags','Tail twitches','Approaches','Indifferent','Runs from'])
            
            for s in squirrels:
                output.writerow([s.X,s.Y,s.Unique_Squirrel_ID,
                    s.Shift,s.Date,
                    s.Age,s.Primary_Fur_Color,
                    s.Location,
                    s.Specific_Location,s.Running,s.Chasing,s.Climbing,s.Eating,
                    s.Foraging,s.Other_Activities,s.Kuks,s.Quaas,s.Moans,
                    s.Tail_flags,s.Approaches,s.Indifferent,s.Runs_from])
            
