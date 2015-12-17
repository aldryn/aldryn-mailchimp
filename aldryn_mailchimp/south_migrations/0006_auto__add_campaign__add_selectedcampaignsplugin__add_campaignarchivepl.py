# -*- coding: utf-8 -*-
from django.db import models

from south.db import db
from south.v2 import SchemaMigration


class Migration(SchemaMigration):
    def forwards(self, orm):
        # Adding model 'Campaign'
        db.create_table(u'aldryn_mailchimp_campaign', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('cid', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('mc_title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('subject', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('send_time', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('content_text', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('content_html', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50)),
            ('hidden', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'aldryn_mailchimp', ['Campaign'])

        # Adding model 'SelectedCampaignsPlugin'
        db.create_table(u'aldryn_mailchimp_selectedcampaignsplugin', (
            (u'cmsplugin_ptr',
             self.gf('django.db.models.fields.related.OneToOneField')(to=orm['cms.CMSPlugin'], unique=True,
                                                                      primary_key=True)),
        ))
        db.send_create_signal(u'aldryn_mailchimp', ['SelectedCampaignsPlugin'])

        # Adding M2M table for field campaigns on 'SelectedCampaignsPlugin'
        m2m_table_name = db.shorten_name(u'aldryn_mailchimp_selectedcampaignsplugin_campaigns')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            (
                'selectedcampaignsplugin',
                models.ForeignKey(orm[u'aldryn_mailchimp.selectedcampaignsplugin'], null=False)),
            ('campaign', models.ForeignKey(orm[u'aldryn_mailchimp.campaign'], null=False))
        ))
        db.create_unique(m2m_table_name, ['selectedcampaignsplugin_id', 'campaign_id'])

        # Adding model 'CampaignArchivePlugin'
        db.create_table(u'aldryn_mailchimp_campaignarchiveplugin', (
            (u'cmsplugin_ptr',
             self.gf('django.db.models.fields.related.OneToOneField')(to=orm['cms.CMSPlugin'], unique=True,
                                                                      primary_key=True)),
            ('count', self.gf('django.db.models.fields.PositiveSmallIntegerField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'aldryn_mailchimp', ['CampaignArchivePlugin'])

    def backwards(self, orm):
        # Deleting model 'Campaign'
        db.delete_table(u'aldryn_mailchimp_campaign')

        # Deleting model 'SelectedCampaignsPlugin'
        db.delete_table(u'aldryn_mailchimp_selectedcampaignsplugin')

        # Removing M2M table for field campaigns on 'SelectedCampaignsPlugin'
        db.delete_table(db.shorten_name(u'aldryn_mailchimp_selectedcampaignsplugin_campaigns'))

        # Deleting model 'CampaignArchivePlugin'
        db.delete_table(u'aldryn_mailchimp_campaignarchiveplugin')

    models = {
        u'aldryn_mailchimp.campaign': {
            'Meta': {'ordering': "['-send_time']", 'object_name': 'Campaign'},
            'cid': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'content_html': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'content_text': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'hidden': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mc_title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'send_time': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'subject': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'aldryn_mailchimp.campaignarchiveplugin': {
            'Meta': {'object_name': 'CampaignArchivePlugin', '_ormbases': ['cms.CMSPlugin']},
            u'cmsplugin_ptr': ('django.db.models.fields.related.OneToOneField', [],
                               {'to': "orm['cms.CMSPlugin']", 'unique': 'True', 'primary_key': 'True'}),
            'count': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        u'aldryn_mailchimp.selectedcampaignsplugin': {
            'Meta': {'object_name': 'SelectedCampaignsPlugin', '_ormbases': ['cms.CMSPlugin']},
            'campaigns': ('django.db.models.fields.related.ManyToManyField', [],
                          {'to': u"orm['aldryn_mailchimp.Campaign']", 'symmetrical': 'False'}),
            u'cmsplugin_ptr': ('django.db.models.fields.related.OneToOneField', [],
                               {'to': "orm['cms.CMSPlugin']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'aldryn_mailchimp.subscriptionplugin': {
            'Meta': {'object_name': 'SubscriptionPlugin', '_ormbases': ['cms.CMSPlugin']},
            'assign_language': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            u'cmsplugin_ptr': ('django.db.models.fields.related.OneToOneField', [],
                               {'to': "orm['cms.CMSPlugin']", 'unique': 'True', 'primary_key': 'True'}),
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
            'parent': ('django.db.models.fields.related.ForeignKey', [],
                       {'to': "orm['cms.CMSPlugin']", 'null': 'True', 'blank': 'True'}),
            'placeholder': (
                'django.db.models.fields.related.ForeignKey', [], {'to': "orm['cms.Placeholder']", 'null': 'True'}),
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
