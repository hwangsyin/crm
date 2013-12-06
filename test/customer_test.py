import os
import sys

home = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(home)

import settings
import environment

from service import customer_service

page_num = 1
customers = customer_service.find_page(page_num)

customer_id = 2
customer = customer_service.find(customer_id)
print(customer.phone)

print(customer.type.repr_json())
