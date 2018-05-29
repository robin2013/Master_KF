from sqlalchemy.dialects.mysql import json

from app import db

detail = {
  'offset':1,
  'limit':12,
  'count': 99,
  'now':'',
  'rows': [
      {
          'id':1,
          'comment': '这是一条评论信息',
          'create_at':'',
          'user':{
              'name': 'robin',
              'image':'http://www.ghost64.com/qqtupian/zixunImg/local/2017/08/08/1502123665822.jpg'
          }

      },
      {
          'id':1,
          'comment': '这是一条评论信息',
          'create_at':'',
          'user':{
              'name': 'robin',
              'image':'http://www.ghost64.com/qqtupian/zixunImg/local/2017/08/08/1502123665822.jpg'
          }
      }
    ]
}

from flask import render_template, flash, jsonify, json
from app.models.Comment import Comment
from . import api
from flask_httpauth import HTTPBasicAuth
auth = HTTPBasicAuth()

@api.route('/comments')
# @auth.login_required
def get_comments():
    # return jsonify({'message': 'users', 'code': 0, 'data': detail})
    coms = Comment.query.all()
    return jsonify({'message': 'ok', 'code': 0, 'data': [com.toDict() for com in coms]})

@api.route('/comments', methods=['POST'])
def post_comment():
    db.create_all()
    comp = Comment(comment='dd')
    comp.save()
    print(comp)
    return jsonify({'message': 'comment ok', 'code': 0, 'data': comp.toDict()})
