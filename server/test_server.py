def TestServer(app):
    def _TestServer(host, port):
        print("test server started at {host}:{port}".format(
            host=host, port=port))
        app.run(host=host, port=port, debug=True)

    return _TestServer
