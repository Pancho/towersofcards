import logging

from django.core.management.base import NoArgsCommand


from api import ASSETS, mongo


logger = logging.getLogger(__name__)


class Command(NoArgsCommand):
	def handle_noargs(self, **options):
		clean_db()
		populate_db()


def clean_db():
	for asset_name in ASSETS.keys():
		# Get "tables" and then clean them (remove() only deletes all the documents, drop() removes all the indices
		# among the other things, so we can rebuild everything)
		mongo.db[asset_name].drop()


def populate_db():
	for asset_name, assets in ASSETS.items():
		mongo.db[asset_name].insert(assets)
		mongo.db[asset_name].create_index([("slug", mongo.ASC)])