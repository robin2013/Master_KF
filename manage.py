import os
from app import create_app, db
from flask_script import Manager, Shell, Server
from flask_migrate import Migrate, MigrateCommand
from flask_bootstrap import Bootstrap

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
manager = Manager(app)
migrate = Migrate(app, db)
bootstrap = Bootstrap(app)

def make_shell_context():
    return dict(app=app, db=db)

manager.add_command('shell',Shell(make_context=make_shell_context))
manager.add_command('db', MigrateCommand)
manager.add_command('runserver', Server(host='0.0.0.0', port=9000, use_debugger=True))

if __name__ == '__main__':
    manager.run()