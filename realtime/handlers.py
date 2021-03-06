import logging


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


class LobbyChatHandler(tornado.websocket.WebSocketHandler):

	lobby_sockets = set()

	def open(self):
		shortcuts.require_login(self)
		logger.info('LobbyChatHandler open for player with username {}'.format(self.player.get('username')))

		LobbyChatHandler.lobby_sockets.add(self)

	def check_origin(self, origin):
		return shortcuts.require_correct_origin(origin)

	def on_message(self, message):
		line = {
			'who': self.player.get('nickname', self.player.get('username')), 
			'what': message,
		}

		logger.info('LobbyChat: {}'.format(line))

		for handler in LobbyChatHandler.lobby_sockets:
			handler.write_message(line)

	def on_close(self):
		logger.info('LobbyChatHandler closed')
		LobbyChatHandler.lobby_sockets.remove(self)
