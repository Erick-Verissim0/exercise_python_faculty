import mysql.connector

connection = mysql.connector.connect(
    host='localhost',
    user='root',
    password='root',
    database='crud_python_prova2'
)

cursor = connection.cursor()

databaseName = 'nome_do_banco_de_dados'
cursor.execute(f"CREATE DATABASE {databaseName}")

connection.commit()

cursor.close()
connection.close()
