from __future__ import unicode_literals

from django.db import models


class Store(models.Model):
    name = models.CharField(max_length=255, unique=True)
    external_id = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return u'{}'.format(self.name)

