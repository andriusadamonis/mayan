from django.conf.urls.defaults import patterns, url


urlpatterns = patterns('main.views',
    url(r'^$', 'home', (), 'home'),
    url(r'^check_settings/$', 'check_settings', (), 'check_settings'),
    url(r'^tools_menu/$', 'blank_menu', (), 'tools_menu'),
    url(r'^statistics/$', 'statistics', (), 'statistics'),
    url(r'^diagnostics/$', 'diagnostics_view', (), 'diagnostics'),
)