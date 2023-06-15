import mysql.connector

connection = mysql.connector.connect(
    host='localhost',
    user='root',
    password='root',
    database='crud_python_prova2'
)

cursor = connection.cursor()

table_collaborators = '''
    CREATE TABLE collaborators (
        id INT PRIMARY KEY AUTO_INCREMENT,
        name VARCHAR(200),
        cpf VARCHAR(14),
        phone VARCHAR(20),
        gender VARCHAR(50),
        idDepartment INT,
        FOREIGN KEY (idDepartment) REFERENCES departments(id)
    )
'''

cursor.execute(table_collaborators)

cursor.close()
connection.close()
