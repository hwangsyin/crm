import settings
import environment

from tornado.web import RequestHandler

from service import customer_service

class CustomerPageHandler(RequestHandler):
    def get(self,page_num = 1):
        print(self.request.uri)
        customers = customer_service.find_page(page_num, settings.settings_app["page_size"])
        self.set_header("Content-Type", "text/html; charset=utf-8")
        self.render("customer_list.tpl", customer_list = customers)

class CustomerHandler(RequestHandler):
    def get(self, customer_id = None):
        print("request uri: " + self.request.uri)
        print("request customer id: " + customer_id)

        c = None
        if (customer_id):
            c = customer_service.find(int(customer_id))

        self.render("customer.tpl", customer = c)
