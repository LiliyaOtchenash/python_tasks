from datetime import date
import tornado.escape
import tornado.ioloop
import tornado.web

class VersionHandler(tornado.web.RequestHandler):
    def get(self):
        self.write('Version: 3.5.1. Last_build:' + date.today().iosformat())
        self.set_header('Content-Type', 'text/plain')

class GetGameByIdHandler(tornado.web.RequestHandler):
    def get(self, id):
        response = {'id': int(id),
                    'name': 'Crazy Game',
                    'release_date': date.today().isoformat()}
        self.write(response)

application = tornado.web.Application([
    (r"/getgamebyid/([0-9]+)", GetGameByIdHandler),
    (r"/version", VersionHandler)
])

if __name__ == 'main':
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()