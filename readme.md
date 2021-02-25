# This is the final project of RD PYTHON 2020

A project is a web service for managing departments and employees.
Project has 9 folders(`migrations; rest; service; sql; static; templates; tests; views`).
`Migrations` contain versions of DataBase connected with project, migrations files to manage changes in DB.
`Models` has one python file **db_tables.py** and classes for DB tables(employees and departments).
`Rest` has two **.py** scripts **rest_dep.py** and **rest_emp.py** with functions that return data in JSON format(`api_all_dep` for json response in format 
```{name:department name}```, `api_show_dep` returns ```{name, average salary, number of employees}``` in json, `return_all_emp` return all employees
```{name, salary, department, birth}``` in json, api_show_emp returns the same data, but for one employee. 
`Service` has also 2 files for CRUD operations with data in DB and functions: `new_dep; del_dep; edit_dep; new_emp; del_emp; edit_emp` for adding, deleting and editing data about department or employee.
`SQL` has only **.sqlite3** file, this is DB connected with project. First table is `department` with columns *(id; name)* and the second is `employee` with columns *(id; name; salary; department; birth)*.
In `static` is three **.css** files for HTML templates:
**main.css** it's a basic file,
one for tables(**tables.css**)
and one for inputs(**forms.css**).
`Templates` has 5 **.html** files:
1)**main.html** for searching employees by their birthday;
2)**department.html** for adding a new department;
3)**departments.html** for displaying table with departments;
4)**employee.html** for adding a new employee;
5)**employees.html** for displaying table with employees;.
`Tests` could contain unittests for this web service, but doesn't.
`Views` it's a package with functions for look up data in DB.
Finally **app.py** it's a main script, that run a project.
At **requirements.txt** contain a list of python packages for this project.
