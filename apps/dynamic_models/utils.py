#-*- coding: UTF-8 -*-
from .settings import CONFIG_FILE
from lxml import etree

from django.db.models.fields import (CharField, FloatField,
                                     IntegerField, BooleanField,
                                     DateField, DateTimeField )


def xml_to_field(field_type):
    if field_type == 'int':
        #TODO fix max_length
        field = IntegerField(max_length=5)
    if field_type == 'char':
        #TODO fix max_length
        field = CharField(max_length=80)
    if  field_type == 'boolean':
        field = BooleanField
    if field_type == 'date':
        field = DateField
    if field_type == 'datetime':
        field = DateTimeField
    if field_type == 'float':
        field = FloatField

    return field


def get_model_from_config(config_file=CONFIG_FILE):
    root = etree.parse(config_file)
    models = root.xpath('//root/model')

    for model in models:
        fields = model.getchildren()
        fields_dict = {}

        for field in fields:
            f = {field.attrib['id']:xml_to_field(field.attrib['type'])}
            fields_dict.update(f)
            result = {
                'name': model.attrib['name'],
                'verbose_name': model.attrib['title'],
                'fields':fields_dict
            }
        yield result
