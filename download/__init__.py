from flask import Flask
from .boxoffice import *

app = Flask(__name__)

app.add_url_rule('/download/box-office/cn/day-cinema', view_func=DayCinema.as_view('csv_cinema_day'))
app.add_url_rule('/download/box-office/cn/day', view_func=DayBoxOffice.as_view('csv_box_office_day'))
app.add_url_rule('/download/box-office/cn/month', view_func=MonthBoxOffice.as_view('csv_box_office_month'))
app.add_url_rule('/download/box-office/cn/realtime', view_func=RealtimeBoxOffice.as_view('csv_box_office_realtime'))
