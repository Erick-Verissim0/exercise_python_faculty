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
    newCpf = input('Qual será o novo cpf? ')

    command = f'UPDATE clients SET cpf = {newCpf} WHERE cpf = "{cpf}"'
    cursor.execute(command)
    connection.commit()

    print('Cliente atualizado com sucesso!')

# DELETE

if numberDigited == '4':
    name = input('Digite o nome do usuário que será deletado: ')
    command = f'DELETE FROM clients WHERE name = "{name}"'
    cursor.execute(command)
    connection.commit()

    print('Cliente deletado com sucesso!')

cursor.close()
connection.close()
