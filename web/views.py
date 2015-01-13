import random
import string
import datetime
import logging


from django.shortcuts import render
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from mongoengine.django.auth import User


# from api import decorators
# from api import mongo
from towersofcards import settings


TEN_YEARS = 10 * 365 * 24 * 60 * 60  # Yes, if this is interesting for 10 years, I'd be totally happy!
ONE_DAY = datetime.timedelta(days=1)


logger = logging.getLogger(__name__)


def login(request):
	next = request.GET.get('next')

	cookies = request.COOKIES
	if 'towersofcards-username' not in cookies:
		new_user = User()
		random_username = ''.join(random.sample(string.ascii_lowercase * 30, 20))
		new_user.username = random_username
		new_user.is_active = True
		new_user.is_staff = False
		new_user.is_superuser = False
		new_user.set_password('password')
		new_user.save()

		response = HttpResponseRedirect(next or '/')
		response.set_cookie('towersofcards-username', random_username, max_age=TEN_YEARS, httponly=True)

		auth_login(request, authenticate(username=random_username, password='password'))
	else:
		username = cookies.get('towersofcards-username')
		auth_login(request, authenticate(username=username, password='password'))
		response = HttpResponseRedirect(next or '/')

	return response


@login_required
def index(request):
	logger.info('Rendering game main')
	ctx = {}

	return render(request, 'index.html', ctx)