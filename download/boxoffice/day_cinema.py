__all__ = ["DayCinema"]

import tushare as ts
from flask import request,json
from flask_restful import Resource
from flask.views import MethodView
from flask import make_response

def get_day_cinema(day=None):
    if day == None:
        try:
            result = ts.day_cinema().to_csv()
        except Exception as e:
            result = json.dumps({"error":True,"message":str(e)})
    else:
        try:
            result = ts.day_cinema(day).to_csv()
        except Exception as e:
            result = json.dumps({"error":True,
            "message":"can not get the data, format date as YYYY-M-D,error:{error}".format(error=e.message)})
    return result

class DayCinema(MethodView):
    """获取全国影院单日票房排行数据，默认为上一日，可输入日期参数获取指定日期的数据。

    参数说明：

    date:日期(YYYY-MM-DD),默认为上一日
    返回值说明：

    Attendance 上座率
    AvgPeople 场均人次
    CinemaName 影院名称
    RowNum 排名
    TodayAudienceCount 当日观众人数
    TodayBox 当日票房
    TodayShowCount 当日场次
    price 场均票价（元）
    """
    def get(self):
        date = request.args.get("date")
        response = make_response(get_day_cinema(date))
        response.headers[
            "Content-Disposition"] = "attachment; filename=day_cinema_{date}.csv;".format(date=date)
        return response
        return
