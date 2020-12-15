from flask import render_template, Blueprint
from models.db_tables import Department, Employee


view_departments = Blueprint("view_departments", __name__)


@view_departments.route('/departments')
def show_all_dep():
    """ this function shows all departments from DataBase """
    deps = Department.query.all()
    return render_template('departments.html', deps=deps)


@view_departments.route('/department/<int:_id>')
def show_dep(_id):
    """ this function is used to show department, average salary and number of employees """
    deps = []
    deps.append(Department.query.get(_id))
    number = Employee.query.filter_by(department=Department.query.get(_id).name).count()
    salary = 0
    for elem in Employee.query.filter_by(department=Department.query.get(_id).name):
        salary += elem.salary
    try:
        salary /= number
    except ZeroDivisionError:
        return "There is no employees in this department"
    return render_template('departments.html', deps=deps, number=number, salary=round(salary, 2))
