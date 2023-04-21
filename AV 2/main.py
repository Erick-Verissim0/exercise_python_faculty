import mysql.connector

connection = mysql.connector.connect(
    host='localhost',
    user='root',
    password='root',
    database='crud_python_prova2'
)

cursor = connection.cursor()

# CREATE

name = 'Erick Veríssimo'
cpf = '12345678910'
phone = 40028922

command = f'INSERT INTO clients(name, cpf, phone) VALUES ("{name}", {cpf}, {phone})'

cursor.execute(command)

connection.commit()

# READ

command = f'SELECT * FROM clients;'
cursor.execute(command)
result = cursor.fetchall()
## print(result)

# UPDATE

cpf = '12345678910'
newCpf = '09876543211'

command = f'UPDATE clients SET cpf = {newCpf} WHERE cpf = "{cpf}"'
cursor.execute(command)
connection.commit()


# DELETE

command = f'DELETE FROM clients WHERE name = "Erick Veríssimo"'
cursor.execute(command)
connection.commit()

cursor.close()
connection.close()
