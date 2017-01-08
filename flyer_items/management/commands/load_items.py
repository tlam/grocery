import pprint

from django.core.management.base import BaseCommand
from django.conf import settings
from django.db.utils import IntegrityError
import requests

from flyer_items.models import FlyerItem
from stores.models import Store


class Command(BaseCommand):

    def handle(self, *args, **options):
        store = Store.objects.get(pk=1)
        flyer_id = 991370
        flyer_url = settings.FLYER['url'].format(flyer_id)
        response = requests.get(flyer_url)
        flyer = response.json()

        for flyer_item in flyer['items']:
            try:
                FlyerItem.objects.get(
                    external_id=flyer_item['id'],
                    flyer_id=flyer_id)
                continue
            except FlyerItem.DoesNotExist:
                pass

            url = settings.FLYER['item_url'].format(flyer_item['id'])
            response = requests.get(url)
            data = response.json()
            item = data['item']
            if not item['current_price']:
                continue

            try:
                FlyerItem.objects.create(
                    name=item['name'],
                    description=item['description'],
                    store=store,
                    external_id=item['id'],
                    flyer_id=item['flyer_id'],
                    price=item['current_price'],
                    price_prefix=item['pre_price_text'],
                    price_suffix=item['price_text'],
                    sale_text=item['sale_story'],
                    disclaimer_text=item['disclaimer_text'],
                )
            except IntegrityError:
                continue
            except Exception as e:
                print e.message
                pprint.pprint(item)

