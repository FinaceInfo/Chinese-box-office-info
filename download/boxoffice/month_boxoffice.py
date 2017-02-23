__all__ = ["MonthBoxOffice"]

import tushare as ts
from flask import request,json
from flask_restful import Resource
from flask.views import MethodView
from flask import make_response

def get_month_boxoffice(month=None):
    if month == None:
        result = ts.month_boxoffice().to_csv()
    else:
        try:
            result = ts.month_boxoffice(month).to_csv()
        except Exception as e:
            result = json.dumps({"error":True,"message":"can not get the data, format date as YYYY-M"})
    return result

class MonthBoxOffice(MethodView):
    """获取单月电影票房数据，默认为上一月，可输入月份参数获取指定月度的数据。

    参数说明：

    date:年月(YYYY-MM),默认为上一月
    返回值说明：

    Irank 排名
    MovieName 电影名称
    WomIndex 口碑指数
    avgboxoffice 平均票价
    avgshowcount 场均人次
    box_pro 月度占比
    boxoffice 单月票房(万)
    days 月内天数
    releaseTime 上映日期
    """
    def get(self):
        date = request.args.get("date")
        response = make_response(get_month_boxoffice(date))
        response.headers[
            "Content-Disposition"] = "attachment; filename=month_box_office_{date}.csv;".format(date=date)
        return response
