from app import db
from flask import  url_for
from datetime import datetime

class Medal(db.Model):
    __tablename__ = 'medals'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    intr = db.Column(db.String)
    own = db.Column(db.Boolean)
    gain = db.Column(db.String)
    image_light = db.Column(db.String)
    image_grey = db.Column(db.String)
    created_at = db.Column(db.DateTime, nullable=False,
                           default=datetime.utcnow)

    def __init_(self, name, intr, own, gain, image_light, image_grey):
        self.name=name
        self.intr=intr
        self.own=own
        self.gain=gain
        self.image_light=image_light
        self.image_grey=image_grey

    def __repr__(self):
        return '<Medal %r>' % self.name


    def toDict(self):
        dic = {
            'id': self.id,
            'name': self.name,
            'intr': self.intr,
            'gain': self.gain,
            'own': self.own,
            'image_light': self.image_light,
            'image_grey': self.image_grey,
            'created_at': self.created_at
        }
        return dic

    @staticmethod
    def ready():
        m0 = Medal(name='初阶勋章',
                   intr='初阶武术家',
                   own=True,
                   gain='学习一门武术',
                   image_light=url_for('static', filename='img/medal/medal_Introduction_get.png', _external=True),
                   image_grey=url_for('static', filename='img/medal/medal_Introduction_get.png', _external=True)
                   )
        m1 = Medal(name='高阶勋章',
                   intr='高阶武术家',
                   own=True,
                   gain='学习一门武术',
                   image_light=url_for('static', filename='img/medal/medal_advanced_get.png', _external=True),
                   image_grey=url_for('static', filename='img/medal/medal_advanced_get.png', _external=True)
                   )
        m2 = Medal(name='5阶勋章',
                   intr='5阶武术家',
                   own=True,
                   gain='学习一门武术',
                   image_light=url_for('static', filename='img/medal/medal_progress_5_get.png', _external=True),
                   image_grey=url_for('static', filename='img/medal/medal_progress_5_get.png', _external=True)
                   )
        m3 = Medal(name='10阶勋章',
                   intr='10阶武术家',
                   own=True,
                   gain='学习一门武术',
                   image_light=url_for('static', filename='img/medal/medal_progress_10_get.png', _external=True),
                   image_grey=url_for('static', filename='img/medal/medal_progress_10_get.png', _external=True)
                   )
        m4 = Medal(name='15阶勋章',
                   intr='15阶武术家',
                   own=True,
                   gain='学习一门武术',
                   image_light=url_for('static', filename='img/medal/medal_progress_15_get.png', _external=True),
                   image_grey=url_for('static', filename='img/medal/medal_progress_15_get.png', _external=True)
                   )
        m5 = Medal(name='30阶勋章',
                   intr='30阶武术家',
                   own=True,
                   gain='学习一门武术',
                   image_light=url_for('static', filename='img/medal/medal_progress_30_get.png', _external=True),
                   image_grey=url_for('static', filename='img/medal/medal_progress_30_get.png', _external=True)
                   )
        m6 = Medal(name='50阶勋章',
                   intr='50阶武术家',
                   own=True,
                   gain='学习一门武术',
                   image_light=url_for('static', filename='img/medal/medal_progress_50_get.png', _external=True),
                   image_grey=url_for('static', filename='img/medal/medal_progress_50_get.png', _external=True)
                   )
        db.session.add_all([m0, m1, m2, m3, m4, m5, m6])
        db.session.commit()

