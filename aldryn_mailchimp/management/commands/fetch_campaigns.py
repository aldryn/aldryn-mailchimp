# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand
from django.conf import settings
from django.utils.text import slugify

from pyrate.services import mailchimp

from ...models import Campaign


class Command(BaseCommand):

    def handle(self, *args, **options):
        mc = mailchimp.MailchimpPyrate(settings.MAILCHIMP_API_KEY)

        response = mc.post('campaigns/list')
        for each in response['data']:
            campaign, created = Campaign.objects.get_or_create(cid=each['id'])
            campaign.send_time = each['send_time']
            campaign.mc_title = each['title']
            campaign.subject = each['subject']
            campaign.slug = slugify(each['subject'])[:50]

            # content
            response_content = mc.post('campaigns/content', content={'cid': campaign.cid})
            campaign.content_text = response_content['text']
            campaign.content_html = response_content['html']

            campaign.save()

        print('imported %i campaigns' % len(response['data']))
