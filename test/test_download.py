from . import download
import json

download.testing = True


class TestBoxOfficDownload(object):

    def test_day_cinema(self):
        client = download.test_client()
        received = client.get("/download/box-office/cn/day-cinema")
        data = str(received.data,"utf-8")
        print(data[:10])
        assert data[:10]==",Attendanc"
        received = client.get("/download/box-office/cn/day-cinema",query_string={"date":"2016-12-3"})
        data = str(received.data,"utf-8")
        print(data[:10])
        assert data[:10]==",Attendanc"

    def test_day_boxoffice(self):
        client = download.test_client()
        received = client.get("/download/box-office/cn/day")
        data = str(received.data,"utf-8")
        print(data[:10])
        assert data[:10]==",AvgPrice," or data[:10]=='{"error": '
        received = client.get("/download/box-office/cn/day",query_string={"date":"2016-12-3"})
        data = str(received.data,"utf-8")
        print(data[:10])
        assert data[:10]==",AvgPrice,"

    def test_month_boxoffice(self):
        client = download.test_client()
        received = client.get("/download/box-office/cn/month")
        data = str(received.data,"utf-8")
        print(data[:10])
        assert data[:10]==",Irank,Mov"
        received = client.get("/download/box-office/cn/month",query_string={"date":"2016-12"})
        data = str(received.data,"utf-8")
        print(data[:10])
        assert data[:10]==",Irank,Mov"

    def test_realtime_boxoffice(self):
        client = download.test_client()
        received = client.get("/download/box-office/cn/realtime")
        data = str(received.data,"utf-8")
        print(data[:10])
        assert data[:10]==",BoxOffice"
