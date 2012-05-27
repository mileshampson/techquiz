from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'djangosite.views.about'),
    url(r'^quiz/(?P<tag>\w+)/$', 'djangosite.views.quiz'),
    url(r'^questions$', 'djangosite.views.index'),
    url(r'^questions/(?P<qid>\d)/$', 'djangosite.views.index'),
    url(r'^new$', 'djangosite.views.new'),
    url(r'^category$', 'djangosite.views.category_select'),
    url(r'^edit$', 'djangosite.views.edit'),
    url(r'^delete$', 'djangosite.views.delete'),
    url(r'^statistics$', 'djangosite.views.statistics'),
    url(r'^admin$', 'djangosite.views.admin'),
    url(r'^about$', 'djangosite.views.about'),
    #url(r'^geolocation$', 'djangosite.views.geolocation'),
    # url(r'^$', 'djangosite.views.home', name='home'),
    # url(r'^djangosite/', include('djangosite.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
