# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import adminsortable.fields


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '__latest__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Campaign',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cid', models.CharField(verbose_name='campaign id', max_length=255, editable=False)),
                ('mc_title', models.CharField(verbose_name='campaign title', max_length=255, editable=False)),
                ('subject', models.CharField(verbose_name='subject', max_length=255, null=True, editable=False, blank=True)),
                ('display_name', models.CharField(max_length=255, null=True, verbose_name='display name', blank=True)),
                ('send_time', models.DateTimeField(verbose_name='time sent', null=True, editable=False, blank=True)),
                ('content_text', models.TextField(verbose_name='content text', null=True, editable=False, blank=True)),
                ('content_html', models.TextField(verbose_name='content HTML', null=True, editable=False, blank=True)),
                ('slug', models.SlugField(verbose_name='slug (generated)', editable=False)),
                ('hidden', models.BooleanField(default=False, verbose_name='hidden')),
            ],
            options={
                'ordering': ['-send_time'],
                'verbose_name': 'Campaign',
                'verbose_name_plural': 'Campaigns',
            },
        ),
        migrations.CreateModel(
            name='CampaignArchivePlugin',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('count', models.PositiveSmallIntegerField(help_text='Leave blank to display all', null=True, verbose_name='count', blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('order', models.PositiveIntegerField(default=0, editable=False, db_index=True)),
                ('name', models.CharField(max_length=255, verbose_name='name')),
                ('smart_match', models.BooleanField(default=True, help_text='Match incoming campaigns to categories based on keywords', verbose_name='Matching')),
            ],
            options={
                'ordering': ('order', 'name'),
                'abstract': False,
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Keyword',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('order', models.PositiveIntegerField(default=0, editable=False, db_index=True)),
                ('value', models.CharField(unique=True, max_length=255, verbose_name='value')),
                ('scope_name', models.BooleanField(default=True, verbose_name='search in campaign name')),
                ('scope_subject', models.BooleanField(default=False, verbose_name='search in campaign subject')),
                ('scope_content', models.BooleanField(default=False, verbose_name='search in campaign content')),
                ('category', adminsortable.fields.SortableForeignKey(verbose_name='category', to='aldryn_mailchimp.Category')),
            ],
            options={
                'ordering': ('order', 'value'),
                'abstract': False,
                'verbose_name': 'Keyword',
                'verbose_name_plural': 'Keywords',
            },
        ),
        migrations.CreateModel(
            name='SelectedCampaignsPlugin',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('campaigns', models.ManyToManyField(to='aldryn_mailchimp.Campaign')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='SubscriptionPlugin',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('list_id', models.CharField(max_length=20, verbose_name='List ID')),
                ('assign_language', models.BooleanField(default=True, help_text="Save the user's language based on the page language", verbose_name="Save user's language")),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.AddField(
            model_name='campaignarchiveplugin',
            name='categories',
            field=models.ManyToManyField(to='aldryn_mailchimp.Category', null=True, verbose_name='filter by category/categories', blank=True),
        ),
        migrations.AddField(
            model_name='campaign',
            name='category',
            field=models.ForeignKey(blank=True, to='aldryn_mailchimp.Category', help_text='leave empty to auto-match on import', null=True),
        ),
    ]
