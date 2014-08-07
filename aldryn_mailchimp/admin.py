# -*- coding: utf-8 -*-
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from .models import Campaign


class CampaignAdmin(admin.ModelAdmin):
    list_display = ('subject', 'mc_title', 'send_time', 'hidden')
    search_fields = ('cid', 'subject', 'mc_title')
    list_filter = ('hidden', )
    list_editable = ('hidden', )
    readonly_fields = ('cid', 'mc_title', 'subject', 'send_time', 'content_html', 'content_text', 'slug')

    _fieldsets = (
        (_('MailChimp Info'), {
            'fields': (
                'cid', 'mc_title', 'subject', 'send_time',
            )}
         ),
        (_('Visibility'), {
            'fields': (
                'hidden',
            )}
         ),
        (_('Content'), {
            'classes': ('collapse', ),
            'fields': (
                'content_text', 'content_html',
            )}
         ),
    )

    def get_fieldsets(self, request, obj=None):
        return self._fieldsets

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

admin.site.register(Campaign, CampaignAdmin)
