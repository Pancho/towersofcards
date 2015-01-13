import os
import logging.config


import tornado.ioloop
import tornado.web
import tornado.wsgi
import tornado.httpserver
os.environ['DJANGO_SETTINGS_MODULE'] = 'towersofcards.settings'


from realtime import urls
from towersofcards import settings


logging.config.dictConfig(settings.LOGGING)


if __name__ == "__main__":
	application = tornado.web.Application(urls.URLS)
	server = tornado.httpserver.HTTPServer(application)
	server.listen(settings.TORNADO_PORT)
	if settings.DEBUG:
		instance = tornado.ioloop.IOLoop.instance()
		tornado.ioloop.PeriodicCallback(lambda: None, 500, instance).start()
		instance.start()
	else:
		tornado.ioloop.IOLoop.instance().start()