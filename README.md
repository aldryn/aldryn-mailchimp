# Aldryn MailChimp

Aldryn Locations is the easiest way to integrate Google Maps into [Aldryn](http://aldryn.com) and [django
CMS](http://django-cms) sites via Google's API.

It's fully featured, and includes several plugins to provide support for:

* multiple locations
* location information
* routes and directions
* searching

To activate MailChimp integration:

* provide an `API Key` while installing an app
* create an CMS page for hooking the app (navigate to ``Advanced Settings -> Application`` on CMS edit page)

When all above is done, you can add MailChimp integration plugins to placeholders.

## Categories + Automatic Matching
Version 0.2.4 introduced categories with automatic matching. You can define categories and add keywords to those categories to automatically sort synced campaigns into categories. You can define priorities for both campaigns and their keywords.

### Matching
Once the campaigns have been fetched, the automatic matcher will go through all categories (starting from the top as defined in ``/admin/aldryn_mailchimp/category/``) and scan each campaign for the defined keywords. You can specify keywords to be searched in any or multiple of the following three:

* campaign title
* campaign subject
* campaign content

Once a match is found, the search for the current campaign will be stopped, the found category will be assigned to the campaign and the matcher will then continue with the next campaign.

