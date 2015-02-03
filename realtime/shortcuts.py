import logging
from urllib.parse import urlparse


from api import players
from towersofcards import settings


logger = logging.getLogger(__name__)


def require_login(handler):
	try:
		username = handler.get_cookie('towersofcards-username')
		player = players.get_player_by_username(username)
		handler.player = player
		if player is None:
			handler.close()  # No player, no socket.
	except:
		logger.warn('Tried to open sockets for a player that\'s not logged in or doesn\'t exist any more.')
		handler.close()  # Exception? No socket.


def require_correct_origin(origin):
	return True
#	parsed_url = urlparse(origin)
#	if parsed_url.netloc in settings.ALLOWED_HOSTS:
#		return True
#	else:
#		return False
