# -*- coding: utf-8 -*-

# http://kb.mailchimp.com/article/can-i-see-what-languages-my-subscribers-use#code
MAILCHIMP_LANGUAGES = [
    'en', 'ar', 'af', 'be', 'bg', 'ca', 'zh', 'hr', 'cs', 'da', 'nl', 'et', 'fa', 'fi', 'fr', 'fr_CA', 'de', 'el', 'he',
    'hi', 'hu', 'is', 'id', 'ga', 'it', 'ja', 'km', 'ko', 'lv', 'lt', 'mt', 'ms', 'mk', 'no', 'pl', 'pt', 'pt_PT', 'ro',
    'ru', 'sr', 'sk', 'sl', 'es', 'es_ES', 'sw', 'sv', 'ta', 'th', 'tr', 'uk', 'vi',
]


def get_language_for_code(code):
    if code in MAILCHIMP_LANGUAGES:
        return code
    if code[:2] in MAILCHIMP_LANGUAGES:
        return code[:2]
    return None
