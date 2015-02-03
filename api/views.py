import logging
from datetime import datetime


from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods


from . import decorators
from . import players
from . import mongo


logger = logging.getLogger(__name__)


@login_required
@require_http_methods(['GET'])
@decorators.ajax_required
@decorators.rest
def home(request):
	player = players.get_player(request.user)
	current_date = datetime.utcnow()
	logger.info(current_date)
	logger.info(list(mongo.db.news.find()))
	news = list(mongo.db.news.find({'activeFrom': {'$lte': current_date}, 'activeTill': {'$gte': current_date}}))
	logger.info(news)
	nickname_missing = False

	if player.get('nickname') is None:
		nickname_missing = True

	return {'news': news, 'nicknameMissing': nickname_missing}

@login_required
@require_http_methods(['GET', 'POST'])
@decorators.ajax_required
@decorators.rest
def nick(request):
	player = players.get_player(request.user)

	if request.method == 'GET':
		return {'nickname' : player.get('nickname')}
	elif request.method == 'POST':
		player['nickname'] = request.POST.get("nickname")
		mongo.upsert_blob(mongo.db.players, player, "username")
		return {}
