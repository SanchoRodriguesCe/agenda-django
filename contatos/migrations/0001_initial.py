# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Contatos'
        db.create_table(u'contatos', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nome', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('endereco', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('sexo', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('email', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('numero', self.gf('django.db.models.fields.IntegerField')(max_length=15)),
        ))
        db.send_create_signal(u'contatos', ['Contatos'])


    def backwards(self, orm):
        # Deleting model 'Contatos'
        db.delete_table(u'contatos')


    models = {
        u'contatos': {
            'Meta': {'ordering': "['nome']", 'object_name': 'Contatos'},
            'email': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'endereco': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'numero': ('django.db.models.fields.IntegerField', [], {'max_length': '15'}),
            'sexo': ('django.db.models.fields.CharField', [], {'max_length': '1'})
        }
    }

    complete_apps = ['contatos']