import os
import sys

home = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(home)

import settings
import environment

from service import customer_service

page_no = 1
customers = customer_service.find_page(1)

customer = customer_service.find(1)
print(customer.type.repr_json())
