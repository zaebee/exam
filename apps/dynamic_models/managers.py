#-*- coding: UTF-8 -*-

from django.db import models

class DynamicModelDescriptor(object):
    def __init__(self, model):
        self.model = model

    def __get__(self, instance):
        if instance is None:
            return DynamicModelManager(self.model)
        return DynamicModelManager(self.model, instance)


class DynamicModelManager(models.Manager):
    def __init__(self, model, instance=None):
        super(DynamicModelManager, self).__init__()
        self.model = model
        self.instance = instance

    def get_query_set(self):
        if self.instance is None:
            return super(DynamicModelManager, self).get_query_set()

        filter = {self.instance._meta.pk.name: self.instance.pk}
        return super(DynamicModelManager, self).get_query_set().filter(**filter)
