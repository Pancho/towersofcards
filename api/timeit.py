import datetime
import logging


logger = logging.getLogger(__name__)


def timeit(method):
	def timed(*args, **kw):
		ts = datetime.datetime.now()
		result = method(*args, **kw)
		te = datetime.datetime.now()

		logger.info('Method %r took %s to execute' % (method.__name__, te - ts))
		return result

	return timed


def burn(method):
	def timed(*args, **kw):
		# repeats = 100
		repeats = 1000
		# repeats = 10000
		# repeats = 100000
		# repeats = 1000000
		times = []

		ts = datetime.datetime.now()

		for i in range(repeats):
			ts_burn = datetime.datetime.now()
			method(*args, **kw)
			te_burn = datetime.datetime.now()

			times.append(te_burn - ts_burn)

		te = datetime.datetime.now()

		logger.info('{} repeats of method {} took {} to execute'.format(repeats, method.__name__, te - ts))
		logger.info('Method {} took {} on average to execute'.format(method.__name__, sum(times, datetime.timedelta()) / repeats))
		logger.info('Shortest time: {}, longest time: {}'.format(min(times), max(times)))

	return timed