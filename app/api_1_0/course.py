from flask import render_template, flash, jsonify, url_for

from . import api
from flask_httpauth import HTTPBasicAuth
auth = HTTPBasicAuth()
from app.models.Comment import Comment

detail = {
    'name':'少林大通臂拳',
    'intr_title': '介绍标题',
    'intr_content':'介绍内容',
    'id': 1,
    'intr_image':'http://www.ghost64.com/qqtupian/zixunImg/local/2017/08/08/1502123665822.jpg',
    'course_videos':[
        {
            'name': '少林大通臂拳',
            'content': '少林大通臂拳',
            'video': 'http://v.tiaooo.com/lmhowNz5Y2o_o-BF4PiNpQadmnfr',
            'id':1
        }
    ],
    'party': {
        'name':'名称',
        'intr_title': '介绍标题',
        'intr_content':'介绍内容',
        'id': 1,
        'intr_image':'http://www.ghost64.com/qqtupian/zixunImg/local/2017/08/08/1502123665822.jpg'
    },
    'now':'2018-05-09\'T\' 17:20:08.444z',
    'comments':{
        'count':1,
        'rows': [
            {
                'id':1,
                'comment': '这是一条评论信息',
                'create_at':'2018-05-09\'T\' 17:20:08.444z',
                'user':{
                    'name': 'robin',
                    'image':'http://www.ghost64.com/qqtupian/zixunImg/local/2017/08/08/1502123665822.jpg'
                }

            }
        ]
    }
}
@api.route('/courses/<int:id>')
# @auth.login_required
def get_course(id):
    coms = Comment.query.all()
    array = [com.toDict() for com in coms]
    detail['comments']['rows'] = array
    return jsonify({'message': 'users', 'code': 0, 'data': detail})
    # return jsonify({'message': 'users', 'code': 0, 'data': ''})