from django.conf.urls import patterns, include, url

urlpatterns = patterns('polls.views',
	url(r'^$', 'index'),
	url(r'^(?P<poll_id>\d+)/$', 'detail'),
	url(r'^(?P<poll_id>\d+)/results/(?P<choice_id>\d+)$', 'results'),
	url(r'^(?P<poll_id>\d+)/vote/$', 'vote'),
)
