# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'UsersDynamicModel'
        db.create_table('dynamic_models_usersdynamicmodel', (
            ('name', self.gf('django.db.models.fields.CharField')(max_length=80, null=True, blank=True)),
            ('paycheck', self.gf('django.db.models.fields.IntegerField')(max_length=5, null=True, blank=True)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('dynamic_models', ['UsersDynamicModel'])

        # Adding model 'RoomsDynamicModel'
        db.create_table('dynamic_models_roomsdynamicmodel', (
            ('department', self.gf('django.db.models.fields.CharField')(max_length=80, null=True, blank=True)),
            ('spots', self.gf('django.db.models.fields.IntegerField')(max_length=5, null=True, blank=True)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('dynamic_models', ['RoomsDynamicModel'])

        # Adding model 'OfficiesDynamicModel'
        db.create_table('dynamic_models_officiesdynamicmodel', (
            ('address', self.gf('django.db.models.fields.CharField')(max_length=80, null=True, blank=True)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('dynamic_models', ['OfficiesDynamicModel'])

        # Adding model 'DynamicModel'
        db.create_table('dynamic_models_dynamicmodel', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('dynamic_models', ['DynamicModel'])


    def backwards(self, orm):
        
        # Deleting model 'UsersDynamicModel'
        db.delete_table('dynamic_models_usersdynamicmodel')

        # Deleting model 'RoomsDynamicModel'
        db.delete_table('dynamic_models_roomsdynamicmodel')

        # Deleting model 'OfficiesDynamicModel'
        db.delete_table('dynamic_models_officiesdynamicmodel')

        # Deleting model 'DynamicModel'
        db.delete_table('dynamic_models_dynamicmodel')


    models = {
        'dynamic_models.dynamicmodel': {
            'Meta': {'object_name': 'DynamicModel'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'dynamic_models.officiesdynamicmodel': {
            'Meta': {'ordering': "('-id',)", 'object_name': 'OfficiesDynamicModel'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '80', 'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
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
