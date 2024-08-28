from django.core.management.base import BaseCommand
import csv
from home.models import HospitalName

class Command(BaseCommand):
    help = 'Loads hospital names from a CSV file'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str, help='Path to the csv file containing hospital names')

    def handle(self, *args, **options):
        csv_file_path = options['csv_file']
        with open(csv_file_path, newline='') as csvfile:
            reader = csv.reader(csvfile)
            next(reader)  # Skip the header row
            for row in reader:
                name = row[0]  # Supposons que la colonne contenant les noms est la première colonne
                HospitalName.objects.get_or_create(name=name)
        self.stdout.write(self.style.SUCCESS('Successfully loaded hospital names'))

