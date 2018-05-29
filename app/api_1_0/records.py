record= {
    'id':1,
    'course_plan_day': {
        'minutes': 20
    },
    'title': '刻苦训练',
    'created_at': '2018-05-09 17:20:08.444z'

}

from flask import render_template, flash, jsonify

from . import api
from flask_httpauth import HTTPBasicAuth
auth = HTTPBasicAuth()

@api.route('/records')
# @auth.login_required
def get_records():
    return jsonify({'message': 'ok', 'code': 0, 'data': [record, record]})