from datetime import date
import tornado.escape
import tornado.ioloop
import tornado.web
import tornado.gen
import tornado.httpclient

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

class GetFullPageAsyncHandler(tornado.web.RequestHandler):
    @tornado.gen.coroutine
    def get(self):
        http_client = tornado.httpclient.AsyncHTTPClient()
        http_response = yield http_client.fetch('http://www.drdobbs.com/web-development')
        response = http_response.body.decode().replace(
            'Most Recent Premium Content', 'Most Recent Content')
        self.write(response)
        self.set_header('Content-Type', 'text/html')

class GetFullPageAsyncNewHandler(tornado.web.RequestHandler):
    @tornado.web.asynchronous
    def get(self):
        http_client = tornado.httpclient.AsyncHTTPClient()
        http_client.fetch('http://www.drdobbs.com/web-development', callback=self.on_fetch)

    def on_fetch(self, http_response):
        if http_response.error: raise tornado.web.HTTPError(500)
        response = http_response.body.decode().replace('Most Recent Premium Content', 'Most Recent Content')
        self.write(response)
        self.set_header('Content-Type', 'text/html')
        self.finish()

application = tornado.web.Application([
    (r"/getfullpage", GetFullPageAsyncHandler),
    (r"/getgamebyid/([0-9]+)", GetGameByIdHandler),
    (r"/version", VersionHandler)
])

if __name__ == 'main':
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()