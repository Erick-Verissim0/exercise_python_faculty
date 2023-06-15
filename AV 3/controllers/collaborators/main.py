import mysql.connector

connection = mysql.connector.connect(
    host='localhost',
    user='root',
    password='root',
    database='crud_python_prova2'
)

cursor = connection.cursor()


numberDigited = input(
    'O que você deseja fazer? \n Digite \n "1" Para CRIAR um colaborador \n "2" Para VER um colaborador que já foi registrado \n "3" Para ATUALIZAR um colaborador \n "4" Para DELETAR um colaborador \n')

while numberDigited not in ['1', '2', '3', '4']:
    print('Opção inválida. Por favor, digite novamente.')
    numberDigited = input(
        'O que você deseja fazer? \n Digite \n "1" Para CRIAR um departamento \n "2" Para VER um departamento que já foi registrado \n "3" Para ATUALIZAR um departamento \n "4" Para DELETAR um departamento \n')

# CREATE

if numberDigited == '1':
    name = input('Digite seu nome: ')
    cpf = input('Digite seu cpf: ')
    phone = input('Digite seu número: ')
    gender = input('Digite seu gênero: ')
    idDepartment = input('Digite o id do seu departamento: ')

    command = f'INSERT INTO collaborators(name, cpf, phone, gender, idDepartment) VALUES ("{name}", "{cpf}", "{phone}", "{gender}", "{idDepartment}")'

    cursor.execute(command)

    connection.commit()

    print('Colaborador registrado com sucesso!')

# READ

if numberDigited == '2':

    command = f'SELECT * FROM collaborators;'
    cursor.execute(command)
    result = cursor.fetchall()
    print(result)

# UPDATE

if numberDigited == '3':
    collaborator = input('Qual o gênero do colaborador(a) ')
    newCollaborator = input('Qual será o novo gênero do colaborador(a) ')

    command = f'UPDATE collaborators SET gender = "{newCollaborator}" WHERE gender = "{collaborator}"'
    cursor.execute(command)
    connection.commit()

    print('Colaborador atualizado com sucesso!')

# DELETE

if numberDigited == '4':
    name = input('Qual o nome do colaborador que será deletado? ')
    command = f'DELETE FROM collaborators WHERE name = "{name}"'
    cursor.execute(command)
    connection.commit()

    print('Colaborador deletado com sucesso!')

cursor.close()
connection.close()
