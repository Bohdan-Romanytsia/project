from datetime import timedelta, date
from flask import render_template, request, Blueprint
from models.db_tables import Employee


view_employees = Blueprint("view_employees", __name__)


def daterange(date1, date2):
    """ this function is used to create a list of dates """
    for n in range(int((date2 - date1).days) + 1):
        yield date1 + timedelta(n)


@view_employees.route('/', methods=["GET", "POST"])
def index():
    """ this function is used to search for employees in the DataBase by date of birth """
    if request.method == 'POST':
        _min = list(map(int, request.form['min'].split("-")))
        _max = list(map(int, request.form['max'].split("-")))
        start_dt = date(_min[0], _min[1], _min[2])
        end_dt = date(_max[0], _max[1], _max[2])
        employees_with_filter = []
        dates = []
        for dt in daterange(start_dt, end_dt):
            dates.append(dt.strftime("%Y-%m-%d"))
        for elem in Employee.query.all():
            if elem.birth in dates:
                employees_with_filter.append(elem)
        return render_template('employees.html', employees=employees_with_filter)
    return render_template('main.html')


@view_employees.route('/employees')
def show_all_emp():
    """ this function shows all employees in DataBase """
    return render_template('employees.html', employees=Employee.query.all())


@view_employees.route('/employee/<int:_id>')
def show_emp(_id):
    """ this function shows employee data in the DataBase """
    employees = []
    employees.append(Employee.query.get(_id))
    return render_template('employees.html', employees=employees)
