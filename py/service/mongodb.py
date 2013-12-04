import settings
import environment

from pymongo import MongoClient

client = MongoClient(settings.settings_app["db_url"])
db = client[settings.settings_app["db_name"]]
