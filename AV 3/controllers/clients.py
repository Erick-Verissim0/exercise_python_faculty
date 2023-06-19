import mysql.connector

connection = mysql.connector.connect(
    host='localhost',
    user='root',
    password='root',
    database='Cybersec'
)

cursor = connection.cursor()

numberDigited = input(
    'O que você deseja fazer? \n Digite \n "1" Para CRIAR um cliente \n "2" Para VER um cliente que já foi registrado \n "3" Para ATUALIZAR um cliente \n "4" Para DELETAR um cliente \n')

while numberDigited not in ['1', '2', '3', '4']:
    print('Opção inválida. Por favor, digite novamente.')
    numberDigited = input(
        'O que você deseja fazer?\nDigite:\n"1" Para CRIAR um cliente\n"2" Para VER um cliente que já foi registrado\n"3" Para ATUALIZAR um cliente\n"4" Para DELETAR um cliente\n')

# CREATE

if numberDigited == '1':
    name = input('Digite seu nome: ')
    cpf = input('Digite seu cpf: ')
    phone = input('Digite seu número: ')

    command = f'INSERT INTO clients(name, cpf, phone) VALUES ("{name}", {cpf}, {phone})'

    cursor.execute(command)

    connection.commit()

    print('Cliente registrado com sucesso!')

# READ

if numberDigited == '2':

    command = f'SELECT * FROM clients;'
    cursor.execute(command)
    result = cursor.fetchall()
    print(result)

# UPDATE

if numberDigited == '3':
    cpf = input('Qual o cpf será alterado? ')
    localToChange = input('Qual campo será alterado? ')
    newData = input('Digite o novo dado: ')

    command = f'UPDATE clients SET {localToChange} = "{newData}" WHERE cpf = "{cpf}"'
    cursor.execute(command)
    connection.commit()

    print('Cliente atualizado com sucesso!')

# DELETE

if numberDigited == '4':
    cpf = input('Digite o cpf do usuário que será deletado: ')
    command = f'DELETE FROM clients WHERE cpf = "{cpf}"'
    cursor.execute(command)
    connection.commit()

    print('Cliente deletado com sucesso!')

cursor.close()
connection.close()
