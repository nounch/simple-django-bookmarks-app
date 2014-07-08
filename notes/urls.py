from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('notes.views',
    url(r'^$', 'index'),
    url(r'^(?P<note_id>\d+)/$', 'detail'),
    url(r'^archive/$', 'archive'),
    url(r'^cathegory/(?P<note_cathegory>\w+)/$', 'cathegory'),
    url(r'^rating/(?P<note_rating>\d+)/$', 'rating'),
    url(r'^delete/(?P<deletion_candidate_id>\d+)/$', 'delete'),
)

