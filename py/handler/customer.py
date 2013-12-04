import settings
import environment

from tornado.web import RequestHandler

from service import customer_service

class CustomerPageHandler(RequestHandler):
    def get(self,page_no = 1 ):
        print(page_no)
        customers = customer_service.find_page(settings.settings_app["page_size"], page_no)
        self.set_header("Content-Type", "application/json; charset=utf-8")
        self.write(customer_service.to_json_array(customers))
