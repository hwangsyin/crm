import settings
import environment

import pymongo

from service import db
from domains import Customer

# 客户管理
class CustomerService:

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
        ct = db["customer_type"].find()
        customer_type_map = {}
        for cus_t in ct:
            customer_type_map[cus_t["key"]] = cus_t
        customers = []
        type = None
        for c_doc in cc:
            type = c_doc["type"]
            c_doc["type"] = customer_type_map[type]
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
    
