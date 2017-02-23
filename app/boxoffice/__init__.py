"""获取各个股票的基本数据
通过网络获取国内当前实时票房和近期历史电影票房数据，了解当下电影热度和排片情况，
尤其是上市公司投资出品的电影，可作为短期投资参考。目前主要包括以下类别：

实时票房数据
每日票房数据
月度票房数据
影院日度票房
"""
__all__ = ["BoxOffice"]
from .realtime_boxoffice import *
from .day_boxoffice import *
from .month_boxoffice import *
from .day_cinema import *

from flask_socketio import Namespace, emit

class BoxOffice(Namespace):

    def on_cn_box_office_day(self,date):
        ok = date.get("query")
        if ok == "ok":
            emit('cn_box_office_day', get_day_boxoffice())
        else:
            emit('cn_box_office_day', get_day_boxoffice(ok))

    def on_cn_box_office_month(self,date):
        ok = date.get("query")
        if ok == "ok":
            emit('cn_box_office_month', get_month_boxoffice())
        else:
            emit('cn_box_office_month', get_month_boxoffice(ok))

    def on_cn_box_office_realtime(self,date):
        ok = date.get("query")
        if ok == "ok":
            emit('cn_box_office_realtime', get_realtime_boxoffice())

    def on_cn_day_cinema(self,date):
        ok = date.get("query")
        if ok == "ok":
            emit('cn_day_cinema', get_day_cinema())
        else:
            emit('cn_day_cinema', get_day_cinema(ok))
