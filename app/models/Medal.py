from app import db

class Medal(db.Model):
    __tablename__ = 'medals'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    intr = db.Column(db.String)
    own = db.Column(db.String)
    gain = db.Column(db.String)
    image_light = db.Column(db.String)
    image_grey = db.Column(db.String)
    created_at = db.Column(db.Date)

    def __init_(self, name, intr, own, gain, image_light, image_grey, created_at):
        self.name=name
        self.intr=intr
        self.own=own
        self.gain=gain
        self.image_light=image_light
        self.image_grey=image_grey
        self.created_at=created_at



    from app import db

    class Role(db.Model):
        __tablename__ = 'roles'
        id = db.Column(db.Integer, primary_key=True)
        name = db.Column(db.String(64), unique=True)
        users = db.relationship('User', backref='role')

        def __repr__(self):
            return '<Medal %r>' % self.name
