import settings
import environment

from datetime import datetime
import pymongo

from service import db
from domains import Customer

# 客户管理
class CustomerService:

    def add(self, customer):
        if not customer:
            return None
        customer_id_cursor = db["customer"].find(None, {"_id": False, "id":True}) \
                .sort("id", pymongo.DESCENDING).limit(1)
        if customer_id_cursor.count() < 1:
            return None

        max_customer_id = customer_id_cursor[0]["id"]
        customer_id = max_customer_id + 1
        customer.id = customer_id
        customer.start_time = datetime.now()
        customer.end_time = None
        db["customer"].insert(customer.doc())

        return customer_id

    """ 分页查询客户 """
    def find_page(self, page_num = 1, page_size = settings.settings_app["page_size"], customer_spec = None):
        if page_size < 1:
            return None
        if page_num < 1:
            return None
       
        count = db["customer"].find().count()
        page_count = int(count / page_size) + 1
        if page_count < page_num:
            page_num = page_count
        skip = (page_num - 1) * page_size
        if count < page_size:
            skip = 0
        limit = page_size
        
        spec = None if not customer_spec else customer_spec.spec()
        cc = db["customer"].find(spec, {"_id": False}) \
            .sort("start_time", pymongo.DESCENDING).skip(skip).limit(limit)

        customer_type_map = self.__customer_type__(doc = True)
        customers = []
        for c_doc in cc:
            c_doc["type"] = customer_type_map[c_doc["type"]]
            customers.append(Customer(c_doc))

        return customers

    """ 根据 ID 查找客户 """
    def find(self, id):
        if not id:
            return None
        
        customer_doc_cursor = db["customer"].find({"id": id}, {"_id": False})
        if not customer_doc_cursor or customer_doc_cursor.count() != 1:
            return None

        customer_doc = customer_doc_cursor[0]
        customer_type_doc_cursor = db["customer_type"].find({"key": customer_doc["type"]}, {"_id": False})
        if not customer_type_doc_cursor or customer_type_doc_cursor.count() != 1:
            customer_doc["type"] = None
        else:
            customer_doc["type"] = customer_type_doc_cursor[0]

        return Customer(customer_doc)

    def __customer_type__(self, doc):
        result = {}

        customer_type_cursor = db["customer_type"].find(None, {"_id": False})
        if customer_type_cursor.count() > 0:
            for customer_type_doc in customer_type_cursor:
                result[customer_type_doc["key"]] = customer_type_doc if doc else CustomerType(customer_type_doc)

        return result
