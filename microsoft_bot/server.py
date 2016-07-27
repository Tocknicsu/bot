# -*- coding: utf8 -*-
import tornado.ioloop
import tornado.web
import tornado.netutil
import tornado.httpserver
import signal
import json
import requests
import config
import urllib.parse 

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
        if message['type'] == 'ping':
            print("Ping")
            return
        res = requests.post(config.url, data=config.auth)
        token = json.loads(res.text)['access_token']
        url = "https://%s.botframework.com/v3/conversations/%s/activities/"%(
                urllib.parse.quote(message['channelId']),
                urllib.parse.quote(message['conversation']['id'])
            )
        response = message['text']
        data = { 
                'type': 'message',
                'from': message['recipient'],
                'recipient': message['from'],
                'text': response 
        }
        headers={
            'Content-Type': 'application/json',
            'Authorization': 'Bearer %s'%(token)
        }
        print(url, data)
        res = requests.post(url, headers=headers, data=json.dumps(data))
        print("[%s] %s"%(res.status_code, res.text))

    def get(self):
        print("get")
    
    def post(self):
        message = json.loads(self.request.body.decode('utf8'))
        self.process(message)


if __name__ == "__main__":
    print("server starting")
    app = tornado.web.Application([
        (r"/api/messages", Index),
    ], debug=True)
    global srv
    srv = tornado.httpserver.HTTPServer(app)
    signal.signal(signal.SIGTERM, sig_handler)
    signal.signal(signal.SIGINT, sig_handler)

    srv.listen(3019)
    print("server started")
    tornado.ioloop.IOLoop.instance().start()
