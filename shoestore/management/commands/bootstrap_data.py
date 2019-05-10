from django.core.management.base import BaseCommand
# , CommandError
from shoestore.models import Manufacturer
import argparse


class Command(BaseCommand):
    help = 'Posts new Manufacturer for the shoestore'

    def add_arguments(self, parser, *args, **options):
        print('add_argument WORKS!')
        parser = argparse.ArgumentParser()
        parser.add_argument('id')
        args = parser.parse_args()

    def handle(self, *args, **options):
        for id in options['id']:
            # print('handle')
            manufacturer = Manufacturer.objects.get(id=args.id)
        # args.id = manufacturer.id

        # manufacturer.name = args.name
        # manufacturer.url = args.url

        # try:
        #     manufacturer = Manufacturer.objects.get(pk=id)
        # except Manufacturer.DoesNotExist:
        #     raise CommandError('Manufacturer "%s" does not exist' % id)
