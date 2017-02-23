from gevent.wsgi import WSGIServer


def GeventServer(app):
    def _GeventServer(host, port):
        http_server = WSGIServer((host, port), app)
        print("gevent server started at {host}:{port}".format(
            host=host, port=port))
        http_server.serve_forever()
    return _GeventServer
