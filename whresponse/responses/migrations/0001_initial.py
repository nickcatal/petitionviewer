# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Response'
        db.create_table(u'responses_response', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('petitions', self.gf('django.db.models.fields.TextField')()),
            ('total_signatures', self.gf('django.db.models.fields.IntegerField')()),
            ('response', self.gf('django.db.models.fields.TextField')()),
            ('url', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'responses', ['Response'])


    def backwards(self, orm):
        # Deleting model 'Response'
        db.delete_table(u'responses_response')


    models = {
        u'responses.response': {
            'Meta': {'object_name': 'Response'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'petitions': ('django.db.models.fields.TextField', [], {}),
            'response': ('django.db.models.fields.TextField', [], {}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'total_signatures': ('django.db.models.fields.IntegerField', [], {}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['responses']