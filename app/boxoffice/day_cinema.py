__all__ = ["get_day_cinema"]

import tushare as ts
from flask import json


TRANS = {"AvgPrice": "平均票价",
         "AvpPeoPle": "场均人次",
         "BoxOffice": "单日票房（万）",
         "BoxOffice_Up": "环比变化 （%）",
         "IRank": "排名",
         "MovieDay": "上映天数",
         "MovieName": "影片名",
         "SumBoxOffice": "累计票房(万)",
         "WomIndex": "口碑指数"
         }

def get_day_cinema(day=None):
    if day == None:
        try:
            total = ts.day_boxoffice().to_csv().split()
            head = [TRANS.get(i) for i in total[0].split(",")]
            body = [line.split(",") for line in total[1:]]
            result = {"head": head, "body": body}
        except Exception as e:
            result = {"error": True, "message": e}
    else:
        try:
            total = ts.day_boxoffice(day).to_csv().split()
            head = [TRANS.get(i) for i in total[0].split(",")]
            body = [line.split(",") for line in total[1:]]
            result = {"head": head, "body": body}
        except Exception as e:
            result = {"error": True, "message": "can not get the data, format date as YYYY-M-D"}
    return result
