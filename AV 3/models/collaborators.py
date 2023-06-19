import mysql.connector

connection = mysql.connector.connect(
    host='localhost',
    user='root',
    password='root',
    database='cybersec'
)

cursor = connection.cursor()

table_collaborators = '''
    CREATE TABLE collaborators (
        id INT PRIMARY KEY AUTO_INCREMENT,
        name VARCHAR(200) NOT NULL,
        cpf VARCHAR(14) NOT NULL,
        phone VARCHAR(20) NOT NULL,
        gender VARCHAR(50) NOT NULL,
        idDepartment INT NOT NULL,
        FOREIGN KEY (idDepartment) REFERENCES departments(id)
    )
'''

cursor.execute(table_collaborators)

cursor.close()
connection.close()
