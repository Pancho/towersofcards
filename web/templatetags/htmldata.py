import json


from django import template


from api import encoders


register = template.Library()


DICT_LIST_TUPLE = (list, dict)


@register.filter(name='datajson')
def datajson(blob):
	if isinstance(blob, DICT_LIST_TUPLE):
		return json.dumps(blob, cls=encoders.VersatileJSONEncoder)
	else:
		return blob