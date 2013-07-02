# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'CommandRun.captured_output'
        db.add_column('lizard_management_command_runner_commandrun', 'captured_output',
                      self.gf('django.db.models.fields.TextField')(default=''),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'CommandRun.captured_output'
        db.delete_column('lizard_management_command_runner_commandrun', 'captured_output')


    models = {
        'lizard_management_command_runner.commandrun': {
            'Meta': {'object_name': 'CommandRun'},
            'captured_output': ('django.db.models.fields.TextField', [], {}),
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