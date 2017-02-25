__all__ = ["get_day_cinema"]

import tushare as ts
from flask import json


TRANS = {"Attendance": "上座率",
         "AvgPeople": "场均人次",
         "CinemaName": "影院名称",
         "RowNum": "排名",
         "TodayAudienceCount": "当日观众人数",
         "TodayBox": "当日票房",
         "TodayShowCount": "当日场次",
         "price": "场均票价（元）"
         }


def get_day_cinema(day=None):
    print(day)
    if day == None:
        try:
            total = ts.day_cinema().to_csv().split()
            head = [TRANS.get(i) for i in total[0].split(",")]
            body = [line.split(",") for line in total[1:]]
            result = {"head": head, "body": body}
        except Exception as e:
            result = {"error": "true", "message": str(e)}
    else:
        try:
            total = ts.day_cinema(day).to_csv().split()
            head = [TRANS.get(i) for i in total[0].split(",")]
            body = [line.split(",") for line in total[1:]]
            result = {"head": head, "body": body}
        except Exception as e:
            result = {"error": "true",
                      "message": "can not get the data, format date as YYYY-M-D"}
    print("result")
    print(result)
    return result
