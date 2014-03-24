# -*- coding: utf-8 -*-
from aldryn_client import forms


class Form(forms.BaseForm):
    mailchimp_api_key = forms.CharField('MailChimp API Key', max_length=50)

    def to_settings(self, data, settings):
        settings['MAILCHIMP_API_KEY'] = data['mailchimp_api_key']
        return settings
