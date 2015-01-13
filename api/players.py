import time
import logging
import datetime


from api import mongo


logger = logging.getLogger(__name__)


def get_player(user):
	logger.info('Fetching player with username {}'.format(user.username))
	result = mongo.db.players.find({'username': user.username})
	if result is None or result.count() == 0:
		mongo.db.players.insert(make_new_player(user.username))
		result = mongo.db.players.find({'username': user.username})[0]
	elif result.count() > 1:
		raise Exception('Two player objects bound to one user. Pay immediate attention to this!')
	else:
		result = result[0]

	return result


def get_player_by_username(username):
	return mongo.db.players.find_one({'username': username})


def make_new_player(username):
	return {
		'username': username,
		'joined': datetime.datetime.now(),
	}


def update_player(player):
	if '_id' in player:
		del player['_id']

	mongo.db.players.update({'username': player.get('username')}, {'$set': player})
