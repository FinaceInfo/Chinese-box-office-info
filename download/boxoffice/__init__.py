"""获取各个股票的基本数据
通过网络获取国内当前实时票房和近期历史电影票房数据，了解当下电影热度和排片情况，
尤其是上市公司投资出品的电影，可作为短期投资参考。目前主要包括以下类别：

实时票房数据
每日票房数据
月度票房数据
影院日度票房
"""

from .realtime_boxoffice import *
from .day_boxoffice import *
from .month_boxoffice import *
from .day_cinema import *
