__all__ = ["DayBoxOffice"]

import tushare as ts
from flask import request,json
from flask_restful import Resource

def get_day_boxoffice(day=None):
    if day == None:
        result = ts.day_boxoffice().to_json()
    else:
        try:
            result = ts.day_boxoffice(day).to_json()
        except Exception as e:
            result = json.dumps({"error":True,"message":"can not get the data, format date as YYYY-M-D"})
    return result


class DayBoxOffice(Resource):
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
        return get_day_boxoffice(date)
