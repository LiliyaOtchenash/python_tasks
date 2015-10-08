# in many frameworks the handler would look something like that
def handler_request(self, request):
    answ = self.remote_server.query(request) # запрашивает з другой базы данных или сервера (отправка Http запрос)
    request.write_response(answ)

# whith AIO - thousands of such requests per second
def handler_request(self, request):
    self.remote_server.query_async(request, self.response_received)

def response_received(self, request, answ): ( это  call-backe метод )
    request.write(answ)
