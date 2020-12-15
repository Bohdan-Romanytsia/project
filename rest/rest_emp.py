from flask import jsonify, Blueprint
from models.db_tables import Employee


rest_employees = Blueprint("rest_employees", __name__)


@rest_employees.route('/api/employees')
def return_all_emp():
    """
    this function returns all employees, their names, salaries,
    departments and date of birth in json format
    """
    result = [{"name": elem.name,
               "department": elem.department,
               "salary": elem.salary,
               "birth": elem.birth} for elem in Employee.query.all()]
    return jsonify(result)


@rest_employees.route('/api/employee/<int:_id>')
def api_show_emp(_id):
    """ this function return employees name, salary, department and date of birth in json format """
    employee = Employee.query.get(_id)
    return {"name": employee.name,
            "department": employee.department,
            "salary": employee.salary,
            "birth": employee.birth}
