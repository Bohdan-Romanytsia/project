from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class Department(db.Model):
    """ Table for DataBase with departments """
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    # name_id = db.Column(db.Integer, db.ForeignKey('employee.id'))

    def __init__(self, name):
        self.name = name


class Employee(db.Model):
    """ Table for DataBase with employee and their data """
    id = db.Column(db.Integer, primary_key=True)
    # department = db.relationship("Department", backref="department")
    department = db.Column(db.String(50), nullable=False)
    name = db.Column(db.String(50), nullable=False)
    salary = db.Column(db.Integer, nullable=False)
    birth = db.Column(db.String(10), nullable=False)

    def __init__(self, name, department, salary, birth):
        self.name = name
        self.department = department
        self.salary = salary
        self.birth = birth
