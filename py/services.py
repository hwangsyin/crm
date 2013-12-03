import pymongo
from pymongo import MongoClient

import settings
import environment

from domains import Customer

class CustomerService:
    def add(self, customer):
        client = MongoClient(settings.settings_app["db_url"])
        db = client["crm"]
        db["customer"].insert(customer.to_doc())
        client.close()

    def max_id(self):
        client = MongoClient(settings.settings_app["db_url"])
        db = client["crm"]
        max_id = db["customer"].find({}, {"id": True, "_id": False}).sort("id", pymongo.DESCENDING).limit(1)[0]["id"]
        client.close()

        return max_id

customer_service = CustomerService()
