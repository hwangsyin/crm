import settings
import environment
import urls

import tornado.web
import tornado.ioloop

application = tornado.web.Application(urls.handlers, **settings.settings)

if __name__ == "__main__":
    application.listen(80)
    tornado.ioloop.IOLoop.instance().start()

