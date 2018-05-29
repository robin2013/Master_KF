


train_step = {
    'id':1,
    'sequence':2,
    'minutes': 20,
    'name': 'step',
    'title': '训练计划',
    'video': 'http://v.tiaooo.com/lmhowNz5Y2o_o-BF4PiNpQadmnfr',
    'icon': 'http://www.ghost64.com/qqtupian/zixunImg/local/2017/08/08/1502123665822.jpg',
    'start_time':'',
    'end_time': ''

}

train_detail = { 'id': '',
         'title': '',
         'minutes': '',
         'sequence': '',
         'steps': '',
         'intr': '',
         'course_plan_actions': [
            train_step,
            train_step,
            train_step
         ],
         'percent': '',
         'background_image': '',
         'video': 'http://v.tiaooo.com/lmhowNz5Y2o_o-BF4PiNpQadmnfr',
         'image': 'http://www.ghost64.com/qqtupian/zixunImg/local/2017/08/08/1502123665822.jpg'
         }

plan_item_model = {
    'id':1,
    'sequence':2,
    'minutes': 20,
    'enable': 0,
    'title': '训练计划'
}

course_plan_model = {
    'course_id': 1,
    'id': 1,
    'name': '基础训练',
    'intr_content':'',
    'intr_weeks': '',
    'course_plan_days': [
        plan_item_model,
        plan_item_model,
        plan_item_model
    ],
    'total_minutes': 20,
    'total_days': 9,
    'join_in': 0,
    'background_image': ''
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



from flask import render_template, flash, jsonify

from . import api
from flask_httpauth import HTTPBasicAuth
auth = HTTPBasicAuth()

@api.route('/plans')
# @auth.login_required
def get_plans():
    return jsonify({'message': 'ok', 'code': 0, 'data': course_plan_model})

@api.route('/plans/<int:id>/join', methods=['POST'])
# @auth.login_required
def post_join(id):
    return jsonify({'message': 'ok', 'code': 0, 'data': {'medals': [medal]} })

@api.route('/plans/<int:id>/days/<int:day>')
# @auth.login_required
def get_trains(id, day):
    return jsonify({'message': 'ok', 'code': 0, 'data': train_detail})