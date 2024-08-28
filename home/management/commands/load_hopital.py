# home/management/commands/load_hospitals.py
from django.core.management.base import BaseCommand
import csv
from home.models import Hospital

class Command(BaseCommand):
    help = 'Loads hospital ids from a CSV file'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str, help='Path to the csv file containing hospital ids')

    def handle(self, *args, **options):
        with open(options['csv_file'], newline='') as csvfile:
            reader = csv.reader(csvfile)
            next(reader)  # Skip the header row
            for row in reader:
                hopital_id = row[0]
                Hospital.objects.get_or_create(hopital_id=hopital_id)
        self.stdout.write(self.style.SUCCESS('Successfully loaded hospital ids'))

