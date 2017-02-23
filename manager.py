from flask_script import Manager, Server
from server import GeventServer, TestServer,TestWsServer,WsServer
from app import app as wsapp
from app import socketio

from api import app as api

from download import app as download

manager = Manager(api)

SERVER = {
    "test": TestServer(app=api),
    "gevent": GeventServer(app=api),
    "testws": TestWsServer(app=wsapp,socketio=socketio),
    "ws": WsServer(app=wsapp,socketio=socketio),
    "testdownload":TestServer(app=download),
    "geventdownload":GeventServer(app=download)
}


@manager.command
def server(choise):
    """can choose from test gevent"""
    print("server start")
    SERVER.get(choise, lambda x, y: print("unknow server"))(
        host="0.0.0.0", port=5000)

if __name__ == "__main__":
    manager.run()
