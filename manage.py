from app import create_app,db
from  flask_migrate import Migrate, MigrateCommand
from app.models import User
from flask_script import Manager,Server
# Creating app instance
app = create_app('production')

manager = Manager(app)
manager.add_command('server',Server)
migrate = Migrate(app,db)
manager.add_command('db',MigrateCommand)
@manager.shell
def make_shell_context():
    return dict(app = app,db = db,User = User )
if __name__ == '__main__':
    app.config['SECRET_KEY'] = 'something only you know'
    app.config["SQLALCHEMY_DATABASE_URI"] ="postgresql+psycopg2://postgres:malcomiz0582@localhost/sql"
    manager.run()