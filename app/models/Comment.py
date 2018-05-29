from datetime import datetime
from flask import  url_for
from flask import  url_for

from app import db

class Comment(db.Model):
    __tablename__ = 'comments'
    id = db.Column(db.Integer, primary_key=True)
    comment = db.Column(db.String(1024))
    created_at = db.Column(db.DateTime, nullable=False,
                         default=datetime.utcnow)

    def __init_(self, comment):
        # self.id=1
        self.comment=comment

    def save(self):
        db.session.add(self)
        db.session.commit()

    def toDict(self):
         dic = {
             'id': self.id,
             'comment': self.comment,
             'created_at': self.created_at,
             'user': {
                 'name': 'robin',
                 'image': url_for('static', filename='img/m1.png', _external=True)
             }
         }
         return dic