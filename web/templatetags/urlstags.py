import logging
import json


from django import template
from django.core.urlresolvers import reverse
from django.utils.html import escape


from api import urls as api_url_specs
from realtime import urls as realtime_url_specs
from towersofcards import settings


logger = logging.getLogger(__name__)
register = template.Library()


@register.simple_tag
def api_urls():
	urls_result = {}

	for url in api_url_specs.urlpatterns:
		if 'api.' in url.name:
			urls_result[url.name.split('.')[-1]] = reverse(url.name)

	if len(urls_result) == 0:
		return ''
	else:
		return ' data-apiurls="{}"'.format(escape(json.dumps(urls_result)))

@register.simple_tag
def realtime_urls():
	urls_result = {}

	for url in realtime_url_specs.URLS:
		urls_result[url.name.split('.')[-1]] = url.reverse()

	if len(urls_result) == 0:
		return ''
	else:
		return ' data-realtimeurls="{}" data-realtimeport="{}"'.format(escape(json.dumps(urls_result)), settings.TORNADO_PORT)