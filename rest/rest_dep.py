from flask import jsonify, Blueprint
from models.db_tables import Department, Employee


rest_departments = Blueprint("rest_departments", __name__)


@rest_departments.route('/api/departments')
def api_all_dep():
    """ this function return all departments in json format """
    deps =[{"department": elem.name} for elem in Department.query.all()]
    return jsonify(deps)


@rest_departments.route('/api/department/<int:_id>')
def api_show_dep(_id):
    """ this function returns department, average salary and number of employees in json format """
    deps = Department.query.get(_id)
    number = Employee.query.filter_by(department=deps.name).count()
    salary = 0
    for elem in Employee.query.filter_by(department=deps.name):
        salary += elem.salary
    try:
        salary /= number
    except ZeroDivisionError:
        return "There is no employees in this department"
    return {"Department": deps.name, "Average_salary": round(salary, 2), "Number_of_employees": number}
