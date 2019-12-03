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
            data = Squirrel()
            output.write(data)
            output.close()
