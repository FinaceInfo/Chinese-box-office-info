from . import api
import json
api.testing = True

class TestBoxOfficeAPI(object):

    def test_day_cinema(self):
        client = api.test_client()
        received = client.get("/api/box-office/cn/day-cinema")
        keys = json.loads(str(received.data,"utf-8")).keys()
        assert ("CinemaName" in keys) or ("error" in keys)
        received = client.get("/api/box-office/cn/day-cinema",
            query_string={"date":"2016-12-3"})
        keys = json.loads(str(received.data,"utf-8")).keys()
        assert ("CinemaName" in keys) or ("error" in keys)

    def test_day_boxoffice(self):
        client = api.test_client()
        received = client.get("/api/box-office/cn/day")
        keys = json.loads(str(received.data,"utf-8")).keys()
        assert "MovieName" in keys
        received = client.get("/api/box-office/cn/day",
            query_string={"date":"2016-12-3"})
        keys = json.loads(str(received.data,"utf-8")).keys()
        assert "MovieName" in keys

    def test_month_boxoffice(self):
        client = api.test_client()
        received = client.get("/api/box-office/cn/month")
        keys = json.loads(str(received.data,"utf-8")).keys()
        assert "MovieName" in keys
        received = client.get("/api/box-office/cn/month",
            query_string={"date":"2016-12"})
        keys = json.loads(str(received.data,"utf-8")).keys()
        assert "MovieName" in keys

    def test_realtime_boxoffice(self):
        client = api.test_client()
        received = client.get("/api/box-office/cn/realtime")
        keys = json.loads(str(received.data,"utf-8")).keys()
        assert "MovieName" in keys
