from flask import render_template, flash

from . import main

from ..models import User, Role
from app import db
from ..models.Medal import Medal
from ..models.TrainStep import TrainStep

@main.route('/initial')
def initial():
    db.drop_all()
    db.create_all()
    Medal.ready()
    TrainStep.ready()
    return render_template('index.html')

@main.route('/')
def index():
    db.create_all()
    return render_template('index.html')

@main.route('/user/<name>')
def user(name):
    flash('Looks like you have changed your name!')
    # insert(name)
    query()
    return render_template('user.html', name=name)

def query():
    result = Role.query.filter_by(name='dd').first()
    users = User.query.filter_by(role=result).all()
    print(users)
    print(result.users)

def insert(name):
    admin_role = Role(name=name)
    user_john = User(username=name, role=admin_role)
    db.session.add(admin_role)
    db.session.add(user_john)

    db.session.commit()
    print(admin_role.id)
    db.session.delete(admin_role)
    db.session.commit()
    print(admin_role.id)