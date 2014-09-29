# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand
from django.conf import settings
from django.utils.text import slugify

from pyrate.services import mailchimp

from ...models import Campaign, Category


class Command(BaseCommand):

    keywords = None

    @staticmethod
    def fetch_keywords():
        keyword_groups = {
            'name': {},
            'subject': {},
            'content': {},
        }

        for category in Category.objects.filter(smart_match=True):
            for kw in category.keyword_set.all():
                if kw.scope_name:
                    keyword_groups['name'][kw.value.lower()] = kw.category.id
                if kw.scope_subject:
                    keyword_groups['subject'][kw.value.lower()] = kw.category.id
                if kw.scope_content:
                    keyword_groups['content'][kw.value.lower()] = kw.category.id
        return keyword_groups

    def search_category(self, campaign):
        attr_list = (
            # kw-group, campaign-attr
            ('name', 'mc_title'),
            ('subject', 'subject'),
            ('content', 'content_text'),
        )

        category_id = None

        for kw_group, campaign_attr in attr_list:
            if not category_id:
                for kw, cat in self.keywords[kw_group].items():
                    if getattr(campaign, campaign_attr) and kw in getattr(campaign, campaign_attr).lower():
                        category_id = cat
                        break

        return category_id

    def handle(self, *args, **options):
        self.keywords = self.fetch_keywords()
        mc = mailchimp.MailchimpPyrate(settings.MAILCHIMP_API_KEY)
        response = mc.post('campaigns/list')
        for each in response['data']:
            campaign, created = Campaign.objects.get_or_create(cid=each['id'])
            campaign.send_time = each['send_time']
            campaign.mc_title = each['title']
            campaign.subject = each['subject']
            campaign.slug = slugify(each['subject'])[:50] if each['subject'] else campaign.pk

            # content
            try:
                response_content = mc.post('campaigns/content', content={'cid': campaign.cid})
            except Exception as e:
                print(e)
                campaign.hidden = True
            else:
                campaign.content_text = response_content['text']
                campaign.content_html = response_content['html']

            # match campaign to category (if not set yet)
            if not campaign.category:
                category_id = self.search_category(campaign)
                if category_id:
                    campaign.category = Category.objects.get(pk=category_id)

            campaign.save()

        print('imported %i campaigns' % len(response['data']))
