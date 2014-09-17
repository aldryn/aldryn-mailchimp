# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Category'
        db.create_table(u'aldryn_mailchimp_category', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('smart_match', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal(u'aldryn_mailchimp', ['Category'])

        # Adding model 'Keyword'
        db.create_table(u'aldryn_mailchimp_keyword', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('value', self.gf('django.db.models.fields.CharField')(unique=True, max_length=255)),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['aldryn_mailchimp.Category'])),
            ('scope_name', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('scope_subject', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('scope_content', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'aldryn_mailchimp', ['Keyword'])

        # Adding field 'Campaign.category'
        db.add_column(u'aldryn_mailchimp_campaign', 'category',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['aldryn_mailchimp.Category'], null=True, blank=True),
                      keep_default=False)


        # Changing field 'Campaign.subject'
        db.alter_column(u'aldryn_mailchimp_campaign', 'subject', self.gf('django.db.models.fields.CharField')(max_length=255, null=True))
        # Adding M2M table for field categories on 'CampaignArchivePlugin'
        m2m_table_name = db.shorten_name(u'aldryn_mailchimp_campaignarchiveplugin_categories')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('campaignarchiveplugin', models.ForeignKey(orm[u'aldryn_mailchimp.campaignarchiveplugin'], null=False)),
            ('category', models.ForeignKey(orm[u'aldryn_mailchimp.category'], null=False))
        ))
        db.create_unique(m2m_table_name, ['campaignarchiveplugin_id', 'category_id'])


    def backwards(self, orm):
        # Deleting model 'Category'
        db.delete_table(u'aldryn_mailchimp_category')

        # Deleting model 'Keyword'
        db.delete_table(u'aldryn_mailchimp_keyword')

        # Deleting field 'Campaign.category'
        db.delete_column(u'aldryn_mailchimp_campaign', 'category_id')


        # Changing field 'Campaign.subject'
        db.alter_column(u'aldryn_mailchimp_campaign', 'subject', self.gf('django.db.models.fields.CharField')(default='unknown', max_length=255))
        # Removing M2M table for field categories on 'CampaignArchivePlugin'
        db.delete_table(db.shorten_name(u'aldryn_mailchimp_campaignarchiveplugin_categories'))


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
            'Meta': {'object_name': 'Category'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'smart_match': ('django.db.models.fields.BooleanField', [], {'default': 'True'})
        },
        u'aldryn_mailchimp.keyword': {
            'Meta': {'object_name': 'Keyword'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['aldryn_mailchimp.Category']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
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