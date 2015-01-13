from tornado.web import URLSpec


from . import handlers


URLS = [
	URLSpec(r'/realtime/test', handlers.TestHandler, name='realtime.test'),
]