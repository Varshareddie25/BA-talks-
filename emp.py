from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)

# Database connection
def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",           # Your MySQL username
        password="varsha",     # Your MySQL password
        database="emp_db"      # Your database name
    )

#  Employee Registration 
@app.route('/register', methods=['GET', 'POST'])
def register_employee():
    if request.method == 'POST':
        name = request.form['name']
        emp_id = request.form['emp_id']
        department = request.form['department']
        designation = request.form['designation']

        conn = get_db_connection()
        cursor = conn.cursor()
        sql = "INSERT INTO employees (name, emp_id, department, designation) VALUES (%s, %s, %s, %s)"
        val = (name, emp_id, department, designation)
        cursor.execute(sql, val)
        conn.commit()

        cursor.close()
        conn.close()
        return "Employee Registered Successfully"

    return render_template('register.html')

# Child Registration 
@app.route('/child', methods=['GET', 'POST'])
def register_child():
    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']
        parent_name = request.form['parent_name']

        conn = get_db_connection()
        cursor = conn.cursor()
        sql = "INSERT INTO child (name, age, parent_name) VALUES (%s, %s, %s)"
        val = (name, age, parent_name)
        cursor.execute(sql, val)
        conn.commit()

        cursor.close()
        conn.close()
        return "Child Registered Successfully"

    return render_template('child.html')

#  Student Registration 
@app.route('/student', methods=['GET', 'POST'])
def register_student():
    if request.method == 'POST':
        name = request.form['name']
        roll_no = request.form['roll_no']
        class_name = request.form['class_name']

        conn = get_db_connection()
        cursor = conn.cursor()
        sql = "INSERT INTO student (name, roll_no, class_name) VALUES (%s, %s, %s)"
        val = (name, roll_no, class_name)
        cursor.execute(sql, val)
        conn.commit()

        cursor.close()
        conn.close()
        return "Student Registered Successfully"

    return render_template('student.html')

if __name__ == "__main__":
    app.run(debug=True)
