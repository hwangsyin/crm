import os
import sys

home = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(home)

import settings
import environment

from service import customer_service
from domains import Customer
from domains import CustomerType

def test_find_page():
    page_num = 1
    customers = customer_service.find_page(page_num)
    print(customers)

def test_find():
    customer_id = 2
    customer = customer_service.find(customer_id)
    print(customer.phone)
    print(customer.type.repr_json())

def test_add():
    customer = Customer(None)
    customer.title = "王先生"
    customer.phone = ["15652318567", "13126714247", "18599392408"]
    customer.name = "王光明"
    customer.age = 33
    customer.email = "billwang@hotmail.com"
    customer.address = "中国北京"
    customer.type = CustomerType(None)
    customer.type.key = "1"
    customer.enable = True

    customer_id = customer_service.add(customer)
    print(customer_id)

test_add()
