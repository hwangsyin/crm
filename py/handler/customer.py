import settings
import environment

from tornado.web import RequestHandler

from service import customer_service

class CustomerHandler(RequestHandler):
    def get(self,page_num = 1):
        customers = customer_service.find_page(page_num, settings.settings_app["page_size"])
        self.set_header("Content-Type", "text/html; charset=utf-8")
        self.render("customer_list.tpl", customer_list = customers)
