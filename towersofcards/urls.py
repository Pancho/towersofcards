from django.conf.urls import patterns, include, url


from towersofcards import settings


urlpatterns = patterns('',
	# WEB
	(r'', include('web.urls')),

	# API
	(r'^api/', include('api.urls')),

	# STATIC CONTENT
	url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
)