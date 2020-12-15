from flask import Flask
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from models.db_tables import db
from views.dep_views import view_departments
from views.emp_views import view_employees
from rest.rest_dep import rest_departments
from rest.rest_emp import rest_employees
from service.dep_operations import crud_dep
from service.emp_operations import crud_emp


def init_db():
    """ this function create database and all tables in it """
    db.app = app
    db.create_all()


if __name__ == '__main__':
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sql/department.sqlite3'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = "random string"

    app.register_blueprint(view_departments)
    app.register_blueprint(view_employees)
    app.register_blueprint(rest_employees)
    app.register_blueprint(rest_departments)
    app.register_blueprint(crud_emp)
    app.register_blueprint(crud_dep)

    db.init_app(app)
    manager = Manager(app)
    migrate = Migrate(app, db)
    manager.add_command('db', MigrateCommand)
    init_db()
    app.run(debug=True, use_reloader=True)
