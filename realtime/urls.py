from tornado.web import URLSpec


from . import handlers


URLS = [
	URLSpec(r'/realtime/test', handlers.TestHandler, name='realtime.test'),
	URLSpec(r'/realtime/lobby-chat', handlers.LobbyChatHandler, name='realtime.lobbychat'),
]
