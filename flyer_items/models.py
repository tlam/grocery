from __future__ import unicode_literals

from django.db import models


class FlyerItem(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(default='')
    store = models.ForeignKey('stores.Store', on_delete=models.CASCADE)
    external_id = models.IntegerField()
    flyer_id = models.IntegerField(default=0)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    price_prefix = models.CharField(max_length=255, default='')
    price_suffix = models.CharField(max_length=255, default='')
    sale_text = models.CharField(max_length=255, default='')
    disclaimer_text = models.TextField(default='')
    image_url = models.CharField(max_length=255, default='')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = (('external_id', 'flyer_id'),)

    def __str__(self):
        return self.name

    def display(self):
        return '{} {} {}'.format(
            self.price_prefix, self.price, self.price_suffix)
