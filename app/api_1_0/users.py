
from flask import render_template, flash, jsonify, url_for

from . import api
from flask_httpauth import HTTPBasicAuth
from ..models.Medal import Medal
from app.models.Comment import Comment

auth = HTTPBasicAuth()

detail= {
    'name': 'robin',
    'uid':'ccccc',
    'image':'http://www.ghost64.com/qqtupian/zixunImg/local/2017/08/08/1502123665822.jpg'
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

records=[
{
    'id':1,
    'course_plan_day': {
        'minutes': 20,
        'title': '刻苦训练'
    },
    'created_at': '2018-05-09 17:20:08.444z'

},
{
    'id':1,
    'course_plan_day': {
        'minutes': 20,
        'title': '中阶训练'
    },
    'created_at': '2018-05-09 17:20:08.444z'

},
{
    'id':1,
    'course_plan_day': {
        'minutes': 20,
        'title': '高阶训练'
    },
    'created_at': '2018-05-09 17:20:08.444z'

}
]
user_mode={
    'name':'Robin',
    'total_days':7,
    'total_times':22,
    'total_minutes':22,
    'medals': [
    ],
    'plans':[
    ],
    'records':{
        'rows':records
    },
    'image':''
}

@api.route('/users')
# @auth.login_required
def get_users():
    medals = Medal.query.all()
    m_dics = [medal.toDict() for medal in medals]
    user_mode['medals'] = m_dics

    user_mode['image'] = url_for('static', filename='img/portrait/personal_head_portrait_1.png', _external=True)
    plan['image'] = url_for('static', filename='img/training_details_image.png', _external=True)
    user_mode['plans'] = [plan]
    return jsonify({'message': 'ok', 'code': 0, 'data': user_mode})

@api.route('/users', methods=['POST'])
# @auth.login_required
def post_nickname():
    return jsonify({'message': 'ok', 'code': 0, 'data': detail })