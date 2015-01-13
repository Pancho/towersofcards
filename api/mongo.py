import sys


import pymongo
from towersofcards import settings



ASC = pymongo.ASCENDING
DSC = pymongo.DESCENDING

db = pymongo.MongoClient(settings.MONGO_DB_ENDPOINT_URL, settings.MONGO_DB_ENDPOINT_PORT)[settings.MONGODB_DB_NAME]


def update_blob(collection, blob):
	collection.update({'_id': blob.pop('_id')}, {'$set': blob})


def upsert_blob(collection, blob, key):
	if '_id' in blob:
		del blob['_id']
	collection.update({key: blob.get(key)}, {'$set': blob}, upsert=True)
