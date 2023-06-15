import mysql.connector

connection = mysql.connector.connect(
    host='localhost',
    user='root',
    password='root',
    database='crud_python_prova2'
)

cursor = connection.cursor()

table_clients = '''
    CREATE TABLE clients (
        id INT PRIMARY KEY AUTO_INCREMENT,
        name VARCHAR(200),
        cpf VARCHAR(14),
        phone VARCHAR(20)
    )
'''

cursor.execute(table_clients)

cursor.close()
connection.close()
