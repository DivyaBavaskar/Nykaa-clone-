import mysql.connector
from flask import Flask, request, render_template

app = Flask(__name__)

# Function to insert form data into the MySQL database
def insert_customers_data(first_name, last_name, email, phone_number, gender):
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='Diyu@123',
        database='nik'
    )
    cursor = connection.cursor()
    sql = 'INSERT INTO customers (first_name, last_name, email, phone_number,gender) VALUES (%s, %s, %s, %s,%s)'
    

    data = (first_name, last_name, email, phone_number,gender)
    cursor.execute(sql, data)
    connection.commit()
    connection.close()

@app.route('/', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        first_name =request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email']
        phone_number = request.form['phone_number']
        gender = request.form['gender']
        
        insert_customers_data(first_name, last_name, email, phone_number, gender)
        return render_template('N2.html')
    
    return render_template('N1.html')


@app.route('/N3')
def N3():
    return render_template('N3.html')

@app.route('/N4')
def N4():
    return render_template('N4.html')

if __name__ == '__main__':
    app.run(debug=True)


# create database nik;
# use nik;

# CREATE TABLE customers (
#    first_Name VARCHAR(50) NOT NULL,
#    last_name VARCHAR(50) NOT NULL,
#    email VARCHAR(100) NOT NULL,
#    phone_number VARCHAR(20
#     gender varchar(15)
#     );
    
#     select * from customers;



