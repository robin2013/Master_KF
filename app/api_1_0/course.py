from flask import render_template, flash, jsonify, url_for

from . import api
from flask_httpauth import HTTPBasicAuth
auth = HTTPBasicAuth()
from app.models.Comment import Comment

detail = {
    'name':'少林大通臂拳',
    'intr_title': '少林通臂拳，是在大通臂和大洪拳的技法是基础上升华而创编的，具有结构严紧，招势大方，猛矫健，攻防兼备,实战性突出的特点',
    'intr_content':'少林通臂拳，是在大通臂和大洪拳的技法是基础上升华而创编的，具有结构严紧，招势大方，猛矫健，攻防兼备,实战性突出的特点'
                   '，特别适于青少年演练·，是中国传统的体育项目。（《现代汉语词典》）武术又称国术或武艺，'
                   '中国传统体育项目。其内容是把踢﹑打﹑摔﹑拿﹑跌﹑击﹑劈﹑刺等动作按照一定规律组成徒手的和器械的各种攻防格斗功夫﹑'
                   '套路和单势练习。有极其广泛的群众基础﹐是汉族劳动人民在长期的社会实践中不断积累和丰富起来的一项宝贵的文化遗产。是中国汉民族的优秀文化遗产之一。',
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
        'name':'武术',
        'intr_title': '武术又称国术或武艺，'
                   '中国传统体育项目。其内容是把踢﹑打﹑摔﹑拿﹑跌﹑击﹑劈﹑刺等动作按照一定规律组成徒手的和器械的各种攻防格斗功夫',
        'intr_content':'武术又称国术或武艺，'
                   '中国传统体育项目。其内容是把踢﹑打﹑摔﹑拿﹑跌﹑击﹑劈﹑刺等动作按照一定规律组成徒手的和器械的各种攻防格斗功夫',
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
    detail['intr_image'] = url_for('static', filename='img/training_details_image.png', _external=True)
    detail['party']['intr_image'] = url_for('static', filename='img/training_details_image.png', _external=True)

    return jsonify({'message': 'users', 'code': 0, 'data': detail})
    # return jsonify({'message': 'users', 'code': 0, 'data': ''})