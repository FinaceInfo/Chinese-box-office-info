__all__ = ["RealtimeBoxOffice"]

import tushare as ts

from flask_restful import Resource

def get_realtime_boxoffice():
    return ts.realtime_boxoffice().to_json()

class RealtimeBoxOffice(Resource):
    """获取实时电影票房数据，30分钟更新一次票房数据，可随时调用。

    返回值说明：

    BoxOffice 实时票房（万）
    Irank 排名
    MovieName 影片名
    boxPer 票房占比 （%）
    movieDay 上映天数
    sumBoxOffice 累计票房（万）
    time 数据获取时间
    """
    def get(self):
        return get_realtime_boxoffice()
