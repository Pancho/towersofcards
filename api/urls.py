from django.conf.urls import patterns, url


urlpatterns = patterns('api.views',
	# Home
	url(r'^home/$', 'home', name='api.home'),
)