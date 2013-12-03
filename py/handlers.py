import settings
import environment

from tornado.web import RequestHandler

from domains import Customer

from services import customer_service

# 首页
class IndexHandler(RequestHandler):
    def get(self):
        self.render(settings.settings_app["index_page"])

# 添加客户UI
class AddCustomerHandler(RequestHandler):
    def get(self):
        self.render("add_customer.html")

# 客户管理
class CustomerHandler(RequestHandler):
    def post(self):
        title = self.get_argument("title", None)
        name = self.get_argument("name", None)
        age = self.get_argument("age", None)
        phone = self.get_argument("phone", None)
        email = self.get_argument("email", None)
        address = self.get_argument("address", None)

        customer = Customer()
        customer.title = title
        customer.name = name
        customer.age = age
        customer.phone = phone
        customer.email = email
        customer.address = address

        customer.id = customer_service.max_id() + 1
        customer_service.add(customer)

        self.redirect("/customers")

    def get(self, customer_id = None):
        print(customer_id)
        self.render("customers.html")
