# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'CommandRun'
        db.create_table('lizard_management_command_runner_commandrun', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('management_command', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['lizard_management_command_runner.ManagementCommand'])),
            ('start_time', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('started_by', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('finished', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('success', self.gf('django.db.models.fields.NullBooleanField')(default=None, null=True, blank=True)),
        ))
        db.send_create_signal('lizard_management_command_runner', ['CommandRun'])


    def backwards(self, orm):
        # Deleting model 'CommandRun'
        db.delete_table('lizard_management_command_runner_commandrun')


    models = {
        'lizard_management_command_runner.commandrun': {
            'Meta': {'object_name': 'CommandRun'},
            'finished': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'management_command': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lizard_management_command_runner.ManagementCommand']"}),
            'start_time': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'started_by': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'success': ('django.db.models.fields.NullBooleanField', [], {'default': 'None', 'null': 'True', 'blank': 'True'})
        },
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