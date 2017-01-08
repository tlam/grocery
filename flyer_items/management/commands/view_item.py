import pprint

from django.conf import settings
from django.core.management.base import BaseCommand
import requests


class Command(BaseCommand):

    def handle(self, *args, **options):
        item_id = 171266044
        url = settings.FLYER['item_url'].format(item_id)
        response = requests.get(url)
        data = response.json()
        pprint.pprint(data)
