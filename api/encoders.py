import json
import decimal
import datetime


from django.utils.timezone import is_aware
from bson import objectid


class VersatileJSONEncoder(json.JSONEncoder):
	"""
	JSONEncoder subclass that knows how to encode date/time, ObjectID and decimal types.
	"""
	def default(self, obj):
		# See "Date Time String Format" in the ECMA-262 specification.
		if isinstance(obj, datetime.datetime):
			r = obj.isoformat()
			if obj.microsecond:
				r = r[:23] + r[26:]
			if r.endswith('+00:00'):
				r = r[:-6] + 'Z'
			return r
		elif isinstance(obj, objectid.ObjectId):
			return str(obj)
		elif isinstance(obj, datetime.date):
			return obj.isoformat()
		elif isinstance(obj, datetime.time):
			if is_aware(obj):
				raise ValueError("JSON can't represent timezone-aware times.")
			r = obj.isoformat()
			if obj.microsecond:
				r = r[:12]
			return r
		elif isinstance(obj, decimal.Decimal):
			return str(obj)
		else:
			return json.JSONEncoder.default(self, obj)