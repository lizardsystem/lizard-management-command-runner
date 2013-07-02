# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'ManagementCommand'
        db.create_table('lizard_management_command_runner_managementcommand', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('command', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('max_minutes_to_run', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('currently_running', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('last_start', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
        ))
        db.send_create_signal('lizard_management_command_runner', ['ManagementCommand'])


    def backwards(self, orm):
        # Deleting model 'ManagementCommand'
        db.delete_table('lizard_management_command_runner_managementcommand')


    models = {
        'lizard_management_command_runner.managementcommand': {
            'Meta': {'object_name': 'ManagementCommand'},
            'command': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'currently_running': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_start': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'max_minutes_to_run': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['lizard_management_command_runner']