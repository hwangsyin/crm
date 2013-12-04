import os

import tornado.web

import settings
import environment
import handlers
from handler.customer import CustomerHandler

handlers = [
    (r"/favicon.ico", tornado.web.RedirectHandler, {"url": "/media/image/favicon.ico"}),
    (r"/media/(.*)", tornado.web.StaticFileHandler, {"path": settings.settings_app["static_file_dir"]}),
    (r"/", handlers.IndexHandler),
    (r"/customers", CustomerHandler),
    (r"/customers/add", handlers.AddCustomerHandler),
    (r"/customers[/](.*)", handlers.CustomerHandler)
]
