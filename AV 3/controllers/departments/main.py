import mysql.connector

connection = mysql.connector.connect(
    host='localhost',
    user='root',
    password='root',
    database='crud_python_prova2'
)

cursor = connection.cursor()


numberDigited = input(
    'O que você deseja fazer? \n Digite \n "1" Para CRIAR um departamento \n "2" Para VER um departamento que já foi registrado \n "3" Para ATUALIZAR um departamento \n "4" Para DELETAR um departamento \n')

while numberDigited not in ['1', '2', '3', '4']:
    print('Opção inválida. Por favor, digite novamente.')
    numberDigited = input(
        'O que você deseja fazer? \n Digite \n "1" Para CRIAR um departamento \n "2" Para VER um departamento que já foi registrado \n "3" Para ATUALIZAR um departamento \n "4" Para DELETAR um departamento \n')

# CREATE

if numberDigited == '1':
    name = input('Digite o nome do departamento: ')

    command = f'INSERT INTO departments(departments) VALUES ("{name}")'

    cursor.execute(command)

    connection.commit()

    print('Departamento registrado com sucesso!')

# READ

if numberDigited == '2':

    command = f'SELECT * FROM departments;'
    cursor.execute(command)
    result = cursor.fetchall()
    print(result)

# UPDATE

if numberDigited == '3':
    department = input('Qual departamento será alterado? ')
    newDepartment = input('Qual será o novo nome do departamento? ')

    command = f'UPDATE departments SET departments = "{newDepartment}" WHERE departments = "{department}"'
    cursor.execute(command)
    connection.commit()

    print('Departamento atualizado com sucesso!')

# DELETE

if numberDigited == '4':
    name = input('Digite o nome do departamento que será deletado: ')
    command = f'DELETE FROM departments WHERE departments = "{name}"'
    cursor.execute(command)
    connection.commit()

    print('Departamento deletado com sucesso!')

cursor.close()
connection.close()
