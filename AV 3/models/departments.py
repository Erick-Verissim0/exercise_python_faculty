import mysql.connector

connection = mysql.connector.connect(
    host='localhost',
    user='root',
    password='root',
    database='crud_python_prova2'
)

cursor = connection.cursor()

table_departments = '''
    CREATE TABLE departments (
        id INT PRIMARY KEY AUTO_INCREMENT,
        department_name VARCHAR(100)
    )
'''

cursor.execute(table_departments)

cursor.close()
connection.close()
