# -*- coding: utf8 -*-
import tornado.ioloop
import tornado.web
import tornado.netutil
import tornado.httpserver
import signal
import json
import requests
import config

import time
import signal


def sig_handler(sig, frame):
    print('Catch Stop Signal')
    tornado.ioloop.IOLoop.instance().add_callback(shutdown)

def shutdown():
    print('Server Stopping')
    global srv
    srv.stop()
    io_loop = tornado.ioloop.IOLoop.instance()
    deadline = time.time() + 3

    def stop_loop():
        now = time.time()
        if now < deadline and (io_loop._callbacks or io_loop._timeouts):
            io_loop.add_timeout(now + 1, stop_loop)
        else:
            io_loop.stop()
            print('Server Stopped')
    stop_loop()

class Index(tornado.web.RequestHandler):
    def process(self, message):
        text = message['content']['text']
        print("From [%s] Text: [%s]"%(message['content']['from'], message['content']['text']))
        ### prepare send data
        ### default response is source text
        response = text
        data = config.data.copy()
        data['to'] = [message['content']['from'],]
        data['content'] = {
            "contentType":1,
            "toType":1, ### can change for other type
            "text": response
        }
        r = requests.post(config.url, headers=config.headers, data=json.dumps(data))
        print("[%s] %s"%(r.status_code, r.text))

    def get(self):
        self.finish("OK")
        print("get")
    
    def post(self):
        message_list = json.loads(self.request.body.decode('utf8'))
        for message in message_list['result']:
            self.process(message)


if __name__ == "__main__":
    print("server starting")
    app = tornado.web.Application([
        (r"/", Index),
    ], debug=True)
    global srv
    srv = tornado.httpserver.HTTPServer(app)
    signal.signal(signal.SIGTERM, sig_handler)
    signal.signal(signal.SIGINT, sig_handler)

    srv.listen(3018)
    print("server started")
    tornado.ioloop.IOLoop.instance().start()
