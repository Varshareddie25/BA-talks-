from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)

def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="varsha",
        database="emp_db"
    )

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        emp_id = request.form['emp_id']
        department = request.form['department']
        designation = request.form['designation']

        # Save to database
        conn = get_db_connection()
        cursor = conn.cursor()
        sql = "INSERT INTO employees (name, emp_id, department, designation) VALUES (%s, %s, %s, %s)"
        val = (name, emp_id, department, designation)
        cursor.execute(sql, val)
        conn.commit()

        # Fetch all employees and print
        cursor.execute("SELECT * FROM employees")
        employees = cursor.fetchall()
        print("\nRegistered Employees:")
        for emp in employees:
            print(emp)

        cursor.close()
        conn.close()

        return "Employee Registered Successfully"

    return render_template('register.html')

if __name__ == "__main__":
    app.run(debug=True)