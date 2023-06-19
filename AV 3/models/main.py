import mysql.connector

connection = mysql.connector.connect(
    host='localhost',
    user='root',
    password='root',
    database='base'
)

cursor = connection.cursor()

databaseName = 'cybersec'
cursor.execute(f"CREATE DATABASE {databaseName}")

connection.commit()

cursor.close()
connection.close()
