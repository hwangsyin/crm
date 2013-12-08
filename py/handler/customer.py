import settings
import environment

from tornado.web import RequestHandler

from service import customer_service
from domains import Customer
from domains import CustomerType

class CustomerPageHandler(RequestHandler):
    def get(self,page_num = 1):
        print(self.request.uri)
        customers = customer_service.find_page(page_num, settings.settings_app["page_size"])
        self.set_header("Content-Type", "text/html; charset=utf-8")
        self.render("customer_list.tpl", customer_list = customers)

    def post(self):
        title = self.get_argument("title", None);
        name = self.get_argument("name", None);
        age = self.get_argument("age", None);
        address = self.get_argument("address", None);
        phone = self.get_argument("phone", None);
        email = self.get_argument("email", None);
        type = self.get_argument("type", None);
        enable = self.get_argument("enable", None);

        customer = Customer(None)
        customer.title = title
        customer.name = name
        customer.age = age
        customer.address = address
        customer.phone = phone.split(",")
        customer.email = email
        customer_type = CustomerType(None)
        customer_type.key = type
        customer.type = customer_type
        customer.enable = enable
        
        customer_service.add(customer)

        self.set_header("Content-Type", "text/plain")
        self.write("成功")


class CustomerHandler(RequestHandler):
    def get(self, customer_id = None):
        print(self.request.uri)

        c = None
        if (customer_id):
            c = customer_service.find(int(customer_id))

        self.render("customer.tpl", customer = c)

class CustomerAddUIHandler(RequestHandler):
    def get(self):
        print(self.request.uri)
        self.set_header("Content-Type", "text/html; charset=UTF-8")
        self.render("add_customer.tpl")
