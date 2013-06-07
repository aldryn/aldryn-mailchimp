# -*- coding: utf-8 -*-
from django import forms
from django.utils.translation import ugettext_lazy as _


class SubscriptionForm(forms.Form):

    email = forms.EmailField(_('E-mail'))
    list_id = forms.CharField(widget=forms.HiddenInput)
    redirect_url = forms.CharField(widget=forms.HiddenInput)
