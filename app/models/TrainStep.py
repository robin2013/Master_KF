from app import db
from flask import  url_for
from datetime import datetime

class TrainStep(db.Model):
    __tablename__ = 'steps'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    title = db.Column(db.String)
    minute = db.Column(db.Integer)
    sequence = db.Column(db.Integer)

    video = db.Column(db.String)
    icon = db.Column(db.String)
    start_time = db.Column(db.DateTime, nullable=False,
                           default=datetime.utcnow)
    end_time = db.Column(db.DateTime, nullable=False,
                           default=datetime.utcnow)

    def __init_(self, name, title, sequence, minute, video, icon):
        self.name=name
        self.sequence=sequence
        self.title=title
        self.minute=minute
        self.video=video
        self.icon=icon


    def __repr__(self):
        return '<Step %r>' % self.name


    def toDict(self):
        dic = {
            'id':self.id,
            'sequence':self.sequence,
            'minute': self.minute,
            'name':  self.name,
            'title': self.title,
            'video': self.video,
            'icon': self.icon,
            'start_time':self.start_time,
            'end_time': self.end_time

        }
        return dic

    @staticmethod
    def ready():
        list = []
        for num in range(1,29):
            filename= 'img/train/train_people_'+ str(num) +'.png'
            url= url_for('static', filename=filename, _external=True)
            obj = TrainStep(name='训练课时'+str(num),
                            sequence=num,
                            minute=num,
                            title='训练科目',
                            video='http://v.tiaooo.com/lmhowNz5Y2o_o-BF4PiNpQadmnfr',
                            icon=url)
            list.append(obj)
        db.session.add_all(list)
        db.session.commit()

