from app import db
from itsdangerous import (TimedJSONWebSignatureSerializer
                          as Serializer, BadSignature, SignatureExpired)
from passlib.apps import custom_app_context as pwd_context
from config import config


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)
    password_hash = db.Column(db.String(64))

    def hash_password(self, password):
        self.password_hash = pwd_context.encrypt(password)

    def verify_password(self, password):
        return pwd_context.verify(password, self.password_hash)

    def generate_auth_token(self, expriration=600):
        s = Serializer(config['SECRET_KEY'], expires_in=expriration)
        return s.dump({'id': self.id})
    # role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
    def __repr__(self):
        return '<User %r>' % self.username

    @staticmethod
    def verify_auth_token(token):
        s = Serializer(config['SECRET_KEY'])
        try:
            data = s.load(token)
        except SignatureExpired:
            return None
        except BadSignature:
            return None

        user = User.query.get
        return user


