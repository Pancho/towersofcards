import logging
import logging.config


import tornado.websocket


from . import shortcuts


logger = logging.getLogger(__name__)


class TestHandler(tornado.websocket.WebSocketHandler):
	def open(self):
		shortcuts.require_login(self)
		logger.info('TestHandler open for player with username {}'.format(self.player.get('username')))

	def check_origin(self, origin):
		return shortcuts.require_correct_origin(origin)

	def on_message(self, message):
		logger.info(message)
		self.write_message("Hello, world")

	def on_close(self):
		logger.info('TestHandler closed')