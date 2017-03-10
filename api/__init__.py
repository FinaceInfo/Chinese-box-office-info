from flask import Flask, make_response, json
from flask_restful import Api
from .boxoffice import *
app = Flask(__name__)
if not app.debug:
    import os
    base_dir = os.path.split(os.path.realpath(__file__))[0]
    import logging
    from logging.handlers import RotatingFileHandler
    file_handler = RotatingFileHandler(base_dir+'/box-office.log', maxBytes=10*1024*1024,backupCount=5)
    file_handler.setLevel(logging.WARNING)
    app.logger.addHandler(file_handler)
api = Api(app)

@api.representation('application/json')
def output_json(data, code, headers=None):
    if isinstance(data, dict):
        resp = make_response(json.dumps(data), code)
    else:
        resp = make_response(data, code)
    resp.headers.extend(headers or {})
    return resp


api.add_resource(RealtimeBoxOffice, '/api/box-office/cn/realtime')
api.add_resource(DayBoxOffice, '/api/box-office/cn/day')
api.add_resource(DayCinema,'/api/box-office/cn/day-cinema')
api.add_resource(MonthBoxOffice,'/api/box-office/cn/month')
