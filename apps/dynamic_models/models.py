#-*- coding: UTF-8 -*-
from django.db import models

from dynamic_models.managers import DynamicModelDescriptor
from dynamic_models.utils import get_model_from_config


class BaseDynamicModel(object):
    registry = {} #register dynamic models

    def contribute_to_class(self, cls, name):
        self.manager_name = name
        models.signals.class_prepared.connect(self.finalize, sender=cls)

    def finalize(self, sender, **kwargs):
        xml_models = get_model_from_config()
        for xml_model in xml_models:
            dynamic_model = self.create_dynamic_model(xml_model)

            descriptor = DynamicModelDescriptor(dynamic_model)
            setattr(sender, self.manager_name, descriptor)

    def create_dynamic_model(self, xml_model=None):
        """
        Creates a dynamic model to associate with the xml model provided.
        """
        attrs = self.get_dynamic_model_fields(xml_model)
        attrs.update(Meta=type('Meta', (), self.get_meta_options(xml_model)))
        name = '%sDynamicModel' % xml_model['name'].title()
        dynamic_model =  type(name, (models.Model,), attrs)
        self.__class__.registry[name] = dynamic_model
        return dynamic_model

    def __contains__(self, module_name):
        return module_name in self.__class__.registry

    def get_dynamic_model(self, module_name):
        return self.__class__.registry.get(module_name)

    def get_dynamic_model_fields(self, xml_model=None):
        """
        Returns a dictionary of fields that will be added to the dynamic
        model.
        """
        fields =  {
            '__module__': self.__module__,

            #primary key field of dynamic item
            'id': models.AutoField(primary_key=True),

            #method of dynamic item
            '__unicode__': lambda self: u'#%d - %s' % (self.id, xml_model['name'])
        }
        #TODO fix adding attribites for field
        #get fields from xml_model
        fields.update(xml_model['fields'])

        return fields

    def get_meta_options(self, xml_model):
        """
        Returns a dictionary of fields that will be added to
        the Meta inner class of the dynamic model.
        """
        return {
            'ordering': ('-id',),
            'verbose_name': u'%s' % xml_model['verbose_name'],
            'verbose_name_plural': u'%s' % xml_model['verbose_name'],
        }


class DynamicModel(models.Model):
    models = BaseDynamicModel()
