__all__ = ["get_month_boxoffice"]

import tushare as ts
from flask import json


TRANS = {"Irank": "排名",
         "MovieName": '电影名称',
         "WomIndex": '口碑指数',
         "avgboxoffice": '平均票价',
         "avgshowcount": "场均人次",
         "box_pro": '月度占比',
         "boxoffice": "单月票房(万)",
         "days": "月内天数",
         "releaseTime": "上映日期"
         }


def get_month_boxoffice(day=None):
    if day == None:
        total = ts.month_boxoffice().to_csv().split()
        head = [TRANS.get(i) for i in total[0].split(",")]
        body = [line.split(",") for line in total[1:]]
        result = {"head": head, "body": body}
    else:
        try:
            total = ts.month_boxoffice(day).to_csv().split()
            head = [TRANS.get(i) for i in total[0].split(",")]
            body = [line.split(",") for line in total[1:]]
            result = {"head": head, "body": body}
        except Exception as e:
            result = {"error": True, "message": "can not get the data, format date as YYYY-M-D"}
    return result
