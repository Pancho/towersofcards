import json
import logging
from functools import wraps


from django.utils.decorators import available_attrs
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseNotAllowed


from . import encoders


logger = logging.getLogger(__name__)
ACCESS_CONTROL_ALLOW_ORIGIN = 'Access-Control-Allow-Origin'
ACCESS_CONTROL_EXPOSE_HEADERS = 'Access-Control-Expose-Headers'
ACCESS_CONTROL_ALLOW_CREDENTIALS = 'Access-Control-Allow-Credentials'
ACCESS_CONTROL_ALLOW_HEADERS = 'Access-Control-Allow-Headers'
ACCESS_CONTROL_ALLOW_METHODS = 'Access-Control-Allow-Methods'
ACCESS_CONTROL_MAX_AGE = 'Access-Control-Max-Age'


def cors(function):
	def wrapper(request, *args, **kwargs):
		response = function(request, *args, **kwargs)

		response[ACCESS_CONTROL_ALLOW_ORIGIN] = '*'
		response[ACCESS_CONTROL_MAX_AGE] = 86400
		response[ACCESS_CONTROL_ALLOW_METHODS] = 'GET, POST, DELETE, OPTIONS'
		response[
			ACCESS_CONTROL_ALLOW_HEADERS] = 'x-requested-with, content-type, accept, origin, authorization, x-csrftoken'
		response[ACCESS_CONTROL_ALLOW_CREDENTIALS] = 'false'
		response[ACCESS_CONTROL_EXPOSE_HEADERS] = ''

		return response
	return wrapper


def ajax_required(function):
	def wrapper(request, *args, **kwargs):
		if not request.is_ajax():
			return HttpResponseBadRequest('AJAX only resource')
		return function(request, *args, **kwargs)

	return wrapper


# Only JSON format supported at this time
def rest(function, result_format='json'):
	def wrapper(request, *args, **kwargs):
		try:
			result = function(request, *args, **kwargs)
			if 'status' not in result:
				result['status'] = 'ok'
			if result_format == 'json':
				return HttpResponse(json.dumps(result, cls=encoders.VersatileJSONEncoder), content_type='application/json')
			else:
				return HttpResponseNotAllowed('Format not supported. JSON only.')
		except Exception as e:  # Cover all exceptions
			logger.error('Error running a rest function')
			logger.error(e)
			raise e

	return wrapper