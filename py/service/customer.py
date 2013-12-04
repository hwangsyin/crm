import settings
import environment

import pymongo

from service import db
from domains import Customer

# 客户管理
class CustomerService:
    def find_page(self, page_no = 1, page_size = settings.settings_app["page_size"], customer_spec = None):
        if page_size < 1:
            return None
        if page_no < 1:
            return None
       
        count = db["customer"].find().count()
        page_count = int(count / page_size) + 1
        if page_count < page_no:
            page_no = page_count
        skip = (page_no - 1) * page_size
        if count < page_size:
            skip = 0
        limit = page_size
        
        spec = None
        if customer_spec:
            spec = customer_spec.spec()
        cc = db["customer"].find(spec, {"_id": False}) \
            .sort("start_time", pymongo.DESCENDING).skip(skip).limit(limit)
        customers = [Customer(c_doc) for c_doc in cc]
        return customers
