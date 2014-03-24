# -*- coding: utf-8 -*-
from django import forms
from django.utils.translation import ugettext_lazy as _


class SubscriptionPluginForm(forms.Form):

    email = forms.EmailField(max_length=100, label=_('E-mail'))
    plugin_id = forms.CharField(widget=forms.HiddenInput)
    redirect_url = forms.CharField(widget=forms.HiddenInput)
