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
            output.writerow(['X','Y','Unique Squirrel ID','Hectare','Shift','Date','Hectare Squirrel Number','Age','Primary Fur Color','Highlight Fur Color','Combination of Primary and Highlight Color','Color notes','Location','Above Ground Sighter Measurement','Specific Location','Running','Chasing','Climbing','Eating','Foraging','Other Activities','Kuks','Quaas','Moans','Tail flags','Tail twitches','Approaches','Indifferent','Runs from','Other Interactions','Lat/Long','Zip Codes','Community Districts','Borough Boundaries','City Council Districts','Police Precincts'])
            
            for s in squirrels:
                output.writerow([s.X,s.Y,s.Unique_Squirrel_ID,
                    s.Hectare,s.Shift,s.Date,s.Hectare_Squirrel_Number,
                    s.Age,s.Primary_Fur_Color,s.Highlight_Fur_Color,
                    s.Combination_of_Primary_and_Highlight_Color,
                    s.Color_notes,s.Location,s.Above_Ground_Sighter_Measurement,
                    s.Specific_Location,s.Running,s.Chasing,s.Climbing,s.Eating,
                    s.Foraging,s.Other_Activities,s.Kuks,s.Quaas,s.Moans,
                    s.Tail_flags,s.Approaches,s.Indifferent,s.Runs_from,s.Other_Interactions,
                    s.Lat_Long,s.Zip_Codes,s.Community_Districts,s.Borough_Boundaries,
                    s.City_Council_Districts,s.Police_Precincts])
            
