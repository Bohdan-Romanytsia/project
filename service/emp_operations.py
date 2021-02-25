from datetime import datetime
from flask import request, flash, url_for, redirect, render_template, Blueprint
from models.db_tables import db, Employee, Department


crud_emp = Blueprint("crud_emp", __name__)


@crud_emp.route('/employee', methods=['GET', 'POST'])
def new_emp():
    """ this function is used to add a new employee in DataBase """
    deps_name = [elem for elem in Department.query.all()]
    if request.method == 'POST':
        if not request.form['name'] or not request.form['salary'] or not request.form['department']:
            flash('Please enter all the fields', 'error')
        else:
            if int(request.form['birth'][:4]) <= datetime.today().year\
                    and int(request.form['birth'][5:7]) <= datetime.today().month\
                    and int(request.form['birth'][8:]) < datetime.today().day:
                birth = request.form['birth']
            else:
                birth = f"{datetime.today().year}-{datetime.today().month}-{datetime.today().day}"
            person = Employee(name=request.form['name'],
                              department=request.form['department'],
                              salary=request.form['salary'],
                              birth=birth)
            try:
                db.session.add(person)
                db.session.commit()
            except:
                flash("The record has not been added")
            return redirect(url_for('view_employees.show_all_emp'))
    return render_template('employee.html', deps=deps_name)


@crud_emp.route('/employee/<int:_id>/del')
def del_emp(_id):
    """ this function is used to remove employee from DataBase """
    employees = Employee.query.get_or_404(_id)
    try:
        db.session.delete(employees)
        db.session.commit()
        return redirect("/employees")
    except:
        return "The record has not been deleted"


@crud_emp.route('/employee/<int:_id>/edit', methods=["POST", "GET"])
def edit_emp(_id):
    """ this function is used to change employees data in the DataBase """
    employee = Employee.query.get(_id)
    deps_name = [elem for elem in Department.query.all()]
    if request.method == "POST":
        employee.name = request.form['name']
        employee.salary = request.form['salary']
        employee.birth = request.form['birth']
        employee.department = request.form['department']
        try:
            db.session.commit()
            return redirect("/employees")
        except:
            return "The record has not been updated"
    else:
        return render_template("employee.html", employee=employee, deps=deps_name)
