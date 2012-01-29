#-*- coding: UTF-8 -*-
from .settings import CONFIG_FILE, MAX_LENGHT_CHAR, MAX_LENGHT_INT
from lxml import etree

from django.db.models.fields import (CharField, FloatField, TextField,
                                     IntegerField, BooleanField,
                                     DateField, DateTimeField )


def xml_to_field(field_type, **kwargs):
    if field_type == 'int':
        #TODO fix max_length
        field = IntegerField(max_length=MAX_LENGHT_INT, **kwargs)
    if field_type == 'char':
        #TODO fix max_length
        field = CharField(max_length=MAX_LENGHT_CHAR, **kwargs)
    if field_type == 'text':
        field = TextField(**kwargs)
    if  field_type == 'boolean':
        field = BooleanField(**kwargs)
    if field_type == 'date':
        field = DateField(**kwargs)
    if field_type == 'datetime':
        field = DateTimeField(**kwargs)
    if field_type == 'float':
        field = FloatField(**kwargs)

    return field


def get_model_from_config(config_file=CONFIG_FILE):
    root = etree.parse(config_file)
    models = root.xpath('//root/model')

    for model in models:
        fields = model.getchildren()
        fields_dict = {}

        for field in fields:
            kwargs = {
                'verbose_name': field.attrib['title'],
                'blank':True,
                'null':True,
                }

            f = {field.attrib['id']:xml_to_field(field.attrib['type'], **kwargs)}
            fields_dict.update(f)

            result = {
                'name': model.attrib['name'],
                'verbose_name': model.attrib['title'],
                'fields':fields_dict
            }
        yield result
