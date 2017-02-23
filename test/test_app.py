from . import wsapp,socketio
import json
wsapp.testing = True

class TestBoxOfficeApp(object):

    def test_day_cinema(self):
        client = socketio.test_client(wsapp, namespace='/boxoffice')
        client.emit('cn_day_cinema', {"query":"ok"}, namespace='/boxoffice')
        received = client.get_received('/boxoffice')
        assert len(received) == 1
        assert len(received[0]['args']) == 1
        assert received[0]['name'] == 'cn_day_cinema'
        assert type(received[0]['args'][0]) == dict

        client.emit('cn_box_office_day', {"query":"2016-12-24"}, namespace='/boxoffice')
        received = client.get_received('/boxoffice')
        assert len(received) == 1
        assert len(received[0]['args']) == 1
        assert received[0]['name'] == 'cn_box_office_day'
        assert type(received[0]['args'][0]) == dict

    def test_day_boxoffice(self):
        client = socketio.test_client(wsapp, namespace='/boxoffice')
        client.emit('cn_box_office_day', {"query":"ok"}, namespace='/boxoffice')
        received = client.get_received('/boxoffice')
        assert len(received) == 1
        assert len(received[0]['args']) == 1
        assert received[0]['name'] == 'cn_box_office_day'
        assert type(received[0]['args'][0]) == dict
        client.emit('cn_box_office_day', {"query":"12-24"}, namespace='/boxoffice')
        received = client.get_received('/boxoffice')
        assert len(received) == 1
        assert len(received[0]['args']) == 1
        assert received[0]['name'] == 'cn_box_office_day'
        assert type(received[0]['args'][0]) == dict

    def test_month_boxoffice(self):
        client = socketio.test_client(wsapp, namespace='/boxoffice')
        client.emit('cn_box_office_month', {"query":"ok"}, namespace='/boxoffice')
        received = client.get_received('/boxoffice')
        assert len(received) == 1
        assert len(received[0]['args']) == 1
        assert received[0]['name'] == 'cn_box_office_month'
        assert type(received[0]['args'][0]) == dict
        client.emit('cn_box_office_month', {"query":"2016-12"}, namespace='/boxoffice')
        received = client.get_received('/boxoffice')
        assert len(received) == 1
        assert len(received[0]['args']) == 1
        assert received[0]['name'] == 'cn_box_office_month'
        assert type(received[0]['args'][0]) == dict

    def test_realtime_boxoffice(self):
        client = socketio.test_client(wsapp, namespace='/boxoffice')
        client.emit('cn_box_office_realtime', {"query":"ok"}, namespace='/boxoffice')
        received = client.get_received('/boxoffice')
        assert len(received) == 1
        assert len(received[0]['args']) == 1
        assert received[0]['name'] == 'cn_box_office_realtime'
        assert type(received[0]['args'][0]) == dict
