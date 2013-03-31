# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Response.slug'
        db.alter_column(u'responses_response', 'slug', self.gf('django.db.models.fields.SlugField')(max_length=250))

    def backwards(self, orm):

        # Changing field 'Response.slug'
        db.alter_column(u'responses_response', 'slug', self.gf('django.db.models.fields.SlugField')(max_length=50))

    models = {
        u'responses.response': {
            'Meta': {'object_name': 'Response'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'petitions': ('django.db.models.fields.TextField', [], {}),
            'response': ('django.db.models.fields.TextField', [], {}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '250'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'total_signatures': ('django.db.models.fields.IntegerField', [], {}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '250'})
        }
    }

    complete_apps = ['responses']