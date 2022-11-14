import csv

from django.core.management.base import BaseCommand
from phones.models import Phone


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('2.1-databases\work_with_database\phones.csv', 'r') as file:
            phones = list(csv.DictReader(file, delimiter=';'))

        for phone in phones:
            item = Phone(
                name = phone['name'],
                price = float(phone['price']),
                image = phone['image'],
                release_date = phone['release_date'],
                lte_exists = eval(phone['lte_exists']),
                slug = phone['name'].lower().replace(" ", "-"),
            )
            item.save()