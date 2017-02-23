from flask import Flask, make_response, json
from flask_restful import Api
from .boxoffice import *
app = Flask(__name__)
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
