__all__ = ["get_realtime_boxoffice"]

import tushare as ts
from flask import json

TRANS = {"BoxOffice": "实时票房（万）",
         "Irank": "排名",
         "MovieName": "影片名",
         "boxPer": "票房占比 （%）",
         "movieDay": "上映天数",
         "sumBoxOffice": "累计票房（万）",
         "time": "数据获取时间"
         }


def get_realtime_boxoffice(day=None):
    try:
        total = ts.realtime_boxoffice().to_csv().split()
        head = [TRANS.get(i) for i in total[0].split(",")]
        body = [line.split(",") for line in total[1:]]
        result = {"head": head, "body": body}
    except Exception as e:
        result = {"error": True, "message": "can not get the data, format date as YYYY-M-D"}
    return result
