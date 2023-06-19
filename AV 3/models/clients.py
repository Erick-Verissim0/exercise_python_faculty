import mysql.connector

connection = mysql.connector.connect(
    host='localhost',
    user='root',
    password='root',
    database='cybersec'
)

cursor = connection.cursor()

table_clients = '''
    CREATE TABLE clients (
        id INT PRIMARY KEY AUTO_INCREMENT,
        name VARCHAR(200) NOT NULL,
        cpf VARCHAR(14) NOT NULL,
        phone VARCHAR(20) NOT NULL
    )
'''

cursor.execute(table_clients)

cursor.close()
connection.close()
