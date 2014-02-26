from django.conf.urls import patterns, url, include


from SomeApplication import views

urlpatterns = patterns('',
    # ex: /SomeApplication/
    url(r'^$', views.index, name='index'),

    url(r'^login/$', views.login, name='login'),
    url(r'^login_post/$', views.login_post, name='login_post'),
    # ex: /SomeApplication/5/
    url(r'^(?P<person_id>\d+)/$', views.dashboard, name='dashboard'),
    # ex: /SomeApplication/dashboard/5/
    url(r'^dashboard/(?P<person_id>\d+)/$', views.dashboard, name='dashboard'),
    url(r'^report/(?P<report_type>[\w])/(?P<person_id>\d+)/(?P<company>[\w]{3})/$', views.report, name='report'),
    url(r'^report_post/$', views.report_post, name='report_post'),
    # ex: /SomeApplication/5/results/
    #url(r'^(?P<company_id>\d+)/results/$', views.results, name='results'),
    # ex: /SomeApplication/5/vote/
    #url(r'^(?P<company_id>\d+)/vote/$', views.vote, name='vote'),

)