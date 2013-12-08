import settings
import environment

from tornado.web import RequestHandler

class SessionAddUIHandler(RequestHandler):
    def get(self):
        print(self.request.uri)
        self.render("add_session.tpl")
