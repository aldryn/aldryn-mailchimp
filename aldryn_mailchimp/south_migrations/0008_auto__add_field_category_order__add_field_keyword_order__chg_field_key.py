# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Category.order'
        db.add_column(u'aldryn_mailchimp_category', 'order',
                      self.gf('django.db.models.fields.PositiveIntegerField')(default=1, db_index=True),
                      keep_default=False)

        # Adding field 'Keyword.order'
        db.add_column(u'aldryn_mailchimp_keyword', 'order',
                      self.gf('django.db.models.fields.PositiveIntegerField')(default=1, db_index=True),
                      keep_default=False)


        # Changing field 'Keyword.category'
        db.alter_column(u'aldryn_mailchimp_keyword', 'category_id', self.gf('adminsortable.fields.SortableForeignKey')(to=orm['aldryn_mailchimp.Category']))

    def backwards(self, orm):
        # Deleting field 'Category.order'
        db.delete_column(u'aldryn_mailchimp_category', 'order')

        # Deleting field 'Keyword.order'
        db.delete_column(u'aldryn_mailchimp_keyword', 'order')


        # Changing field 'Keyword.category'
        db.alter_column(u'aldryn_mailchimp_keyword', 'category_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['aldryn_mailchimp.Category']))

    models = {
        u'aldryn_mailchimp.campaign': {
            'Meta': {'ordering': "['-send_time']", 'object_name': 'Campaign'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['aldryn_mailchimp.Category']", 'null': 'True', 'blank': 'True'}),
            'cid': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'content_html': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'content_text': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'hidden': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mc_title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'send_time': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'subject': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
        },
        u'aldryn_mailchimp.campaignarchiveplugin': {
            'Meta': {'object_name': 'CampaignArchivePlugin', '_ormbases': ['cms.CMSPlugin']},
            'categories': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['aldryn_mailchimp.Category']", 'null': 'True', 'blank': 'True'}),
            u'cmsplugin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cms.CMSPlugin']", 'unique': 'True', 'primary_key': 'True'}),
            'count': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        u'aldryn_mailchimp.category': {
            'Meta': {'ordering': "['order']", 'object_name': 'Category'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'order': ('django.db.models.fields.PositiveIntegerField', [], {'default': '1', 'db_index': 'True'}),
            'smart_match': ('django.db.models.fields.BooleanField', [], {'default': 'True'})
        },
        u'aldryn_mailchimp.keyword': {
            'Meta': {'ordering': "['order']", 'object_name': 'Keyword'},
            'category': ('adminsortable.fields.SortableForeignKey', [], {'to': u"orm['aldryn_mailchimp.Category']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order': ('django.db.models.fields.PositiveIntegerField', [], {'default': '1', 'db_index': 'True'}),
            'scope_content': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'scope_name': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'scope_subject': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'value': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'})
        },
        u'aldryn_mailchimp.selectedcampaignsplugin': {
            'Meta': {'object_name': 'SelectedCampaignsPlugin', '_ormbases': ['cms.CMSPlugin']},
            'campaigns': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['aldryn_mailchimp.Campaign']", 'symmetrical': 'False'}),
            u'cmsplugin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cms.CMSPlugin']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'aldryn_mailchimp.subscriptionplugin': {
            'Meta': {'object_name': 'SubscriptionPlugin', '_ormbases': ['cms.CMSPlugin']},
            'assign_language': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            u'cmsplugin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cms.CMSPlugin']", 'unique': 'True', 'primary_key': 'True'}),
            'list_id': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        },
        'cms.cmsplugin': {
            'Meta': {'object_name': 'CMSPlugin'},
            'changed_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'creation_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'max_length': '15', 'db_index': 'True'}),
            'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cms.CMSPlugin']", 'null': 'True', 'blank': 'True'}),
            'placeholder': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cms.Placeholder']", 'null': 'True'}),
            'plugin_type': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_index': 'True'}),
            'position': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'})
        },
        'cms.placeholder': {
            'Meta': {'object_name': 'Placeholder'},
            'default_width': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slot': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_index': 'True'})
        }
    }

    complete_apps = ['aldryn_mailchimp']