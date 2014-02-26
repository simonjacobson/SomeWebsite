from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'SomeWebsite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^SomeApplication/', include('SomeApplication.urls', namespace='SomeApplication')),
    url(r'^admin/', include(admin.site.urls)),
)
