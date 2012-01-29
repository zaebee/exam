# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'OfficiesDynamicModel.mode'
        db.add_column('dynamic_models_officiesdynamicmodel', 'mode', self.gf('django.db.models.fields.TextField')(null=True, blank=True), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'OfficiesDynamicModel.mode'
        db.delete_column('dynamic_models_officiesdynamicmodel', 'mode')


    models = {
        'dynamic_models.dynamicmodel': {
            'Meta': {'object_name': 'DynamicModel'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'dynamic_models.officiesdynamicmodel': {
            'Meta': {'ordering': "('-id',)", 'object_name': 'OfficiesDynamicModel'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '80', 'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mode': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'})
        },
        'dynamic_models.roomsdynamicmodel': {
            'Meta': {'ordering': "('-id',)", 'object_name': 'RoomsDynamicModel'},
            'department': ('django.db.models.fields.CharField', [], {'max_length': '80', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'spots': ('django.db.models.fields.IntegerField', [], {'max_length': '5', 'null': 'True', 'blank': 'True'})
        },
        'dynamic_models.usersdynamicmodel': {
            'Meta': {'ordering': "('-id',)", 'object_name': 'UsersDynamicModel'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '80', 'null': 'True', 'blank': 'True'}),
            'paycheck': ('django.db.models.fields.IntegerField', [], {'max_length': '5', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['dynamic_models']
