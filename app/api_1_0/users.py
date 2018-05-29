
from flask import render_template, flash, jsonify

from . import api
from flask_httpauth import HTTPBasicAuth
auth = HTTPBasicAuth()

detail= {
    'name': 'robin',
    'uid':'ccccc',
    'image':'http://www.ghost64.com/qqtupian/zixunImg/local/2017/08/08/1502123665822.jpg'
}

medal = {
    'name': '初学者',
    'intr': '初学者',
    'own': 1,
    'gain': '11',
    'image_light':'http://www.ghost64.com/qqtupian/zixunImg/local/2017/08/08/1502123665822.jpg',
    'image_grey':'http://www.ghost64.com/qqtupian/zixunImg/local/2017/08/08/1502123665822.jpg',
    'created_at':'2018-05-09 17:20:08.444z'
}
plan = { 'course_name': '高手竞技',
         'course_plan_id': 11,
         'next_sequence': '13',
         'total_steps': '56',
         'course_plan_days_id': 1,
         'title': '基础训练',
         'updated_at': '2018-05-09 17:20:08.444z',
         'is_rest_day': 1,
         'current_days': 12,
         'percent': 12,
         'total_days': 22,
         'image': ''
         }

record= {
    'id':1,
    'course_plan_day': {
        'minutes': 20
    },
    'title': '刻苦训练',
    'created_at': '2018-05-09 17:20:08.444z'

}
user_mode={
    'name':'Robin',
    'total_days':7,
    'total_times':22,
    'total_minutes':22,
    'medals': [
        medal,
        medal,
        medal
    ],
    'plans':[
        plan,
        plan,
        plan
    ],
    'records':{
        'rows':[
            record,
            record,
            record,
            record
        ]
    },
    'image':'http://www.ghost64.com/qqtupian/zixunImg/local/2017/08/08/1502123665822.jpg'
}

@api.route('/users')
# @auth.login_required
def get_users():
    return jsonify({'message': 'ok', 'code': 0, 'data': user_mode})

@api.route('/users', methods=['POST'])
# @auth.login_required
def post_nickname():
    return jsonify({'message': 'ok', 'code': 0, 'data': detail })