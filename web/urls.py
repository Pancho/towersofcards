from django.conf.urls import patterns, url


urlpatterns = patterns('web.views',
	# Login
	url(r'^login/$', 'login', name='web.login'),
	# Index
	url(r'^$', 'index', name='web.index'),
)