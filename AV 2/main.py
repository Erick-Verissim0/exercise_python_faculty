import mysql.connector

connection = mysql.connector.connect(
    host='localhost',
    user='root',
    password='root',
    database='crud_python_prova2'
)

cursor = connection.cursor()

numberDigited = input(
    'O que você deseja fazer? \n Digite \n "1" Para CRIAR um cliente \n "2" Para VER um cliente que já foi registrado \n "3" Para ATUALIZAR um cliente \n "4" Para DELETAR um cliente \n')

if numberDigited != "1" or "2" or "3" or "4":
    print(' ----------------------------------------------------------')
    print('   O que você digitou não é o esperado, tente novamente!   ')
    print(' ----------------------------------------------------------')

# CREATE

if numberDigited == '1':
    name = 'Erick Veríssimo'
    cpf = '12345678910'
    phone = 40028922

    command = f'INSERT INTO clients(name, cpf, phone) VALUES ("{name}", {cpf}, {phone})'

    cursor.execute(command)

    connection.commit()

# READ

if numberDigited == '2':
    command = f'SELECT * FROM clients;'
    cursor.execute(command)
    result = cursor.fetchall()
    print(result)

# UPDATE

if numberDigited == '3':
    cpf = '12345678910'
    newCpf = '09876543211'

    command = f'UPDATE clients SET cpf = {newCpf} WHERE cpf = "{cpf}"'
    cursor.execute(command)
    connection.commit()


# DELETE

if numberDigited == '4':
    command = f'DELETE FROM clients WHERE name = "Erick Veríssimo"'
    cursor.execute(command)
    connection.commit()

cursor.close()
connection.close()
