__all__ = ["DayBoxOffice"]

import tushare as ts
from flask import request,json
from flask.views import MethodView
from flask import make_response

def get_day_boxoffice(day=None):
    if day == None:
        result = ts.day_boxoffice().to_csv()
    else:
        try:
            result = ts.day_boxoffice(day).to_csv()
        except Exception as e:
            result = json.dumps({"error":True,"message":"can not get the data, format date as YYYY-M-D"})
    return result


class DayBoxOffice(MethodView):
    """获取单日电影票房数据，默认为上一日的电影票房，可输入参数获取指定日期的票房。
    参数说明：

    date: 日期（YYYY-MM-DD）,默认为上一日
    返回值说明：

    AvgPrice 平均票价
    AvpPeoPle 场均人次
    BoxOffice 单日票房（万）
    BoxOffice_Up 环比变化 （%）
    IRank 排名
    MovieDay 上映天数
    MovieName 影片名
    SumBoxOffice 累计票房（万）
    WomIndex 口碑指数
    """
    def get(self):
        date = request.args.get("date")
        response = make_response(get_day_boxoffice(date))
        response.headers[
            "Content-Disposition"] = "attachment; filename=day_box_office_{date}.csv;".format(date=date)
        return response
