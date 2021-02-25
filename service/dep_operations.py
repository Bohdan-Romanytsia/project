from flask import request, flash, url_for, redirect, render_template, Blueprint
from models.db_tables import db, Department, Employee


crud_dep = Blueprint("crud_dep", __name__)


@crud_dep.route('/department', methods=['GET', 'POST'])
def new_dep():
    """ this function is used to create a new department in DataBase """
    if request.method == 'POST':
        if not request.form['name']:
            flash('Please enter department\'s name', 'error')
        else:
            dep = Department(name=request.form['name'])
            exists = Department.query.filter_by(name=request.form['name']).count()
            if not exists:
                try:
                    db.session.add(dep)
                    db.session.commit()
                    return redirect(url_for('view_departments.show_all_dep'))
                except:
                    flash("The record was not been added")
            else:
                flash("A department with this name already exists")
    return render_template('department.html')


@crud_dep.route('/department/<int:_id>/del')
def del_dep(_id):
    """ this function is used to delete department from DataBase """
    depart = Department.query.get_or_404(_id)
    try:
        for emp in Employee.query.filter_by(department=depart.name):
            db.session.delete(emp)
        db.session.delete(depart)
        db.session.commit()
        return redirect("/departments")
    except:
        return "The record has not been deleted"


@crud_dep.route('/department/<int:_id>/edit', methods=["GET", "POST"])
def edit_dep(_id):
    """ this function is used to change department date in DataBase """
    deps = Department.query.get_or_404(_id)
    old_name = deps.name
    if request.method == "POST":
        deps.name = request.form.get('name')
        emp_dep = Employee.query.filter_by(department=old_name)
        for emp in emp_dep:
            emp.department = deps.name
        db.session.commit()
        try:
            return redirect("/departments")
        except:
            flash("The record has not been updated")
    else:
        return render_template("department.html", deps=deps)
