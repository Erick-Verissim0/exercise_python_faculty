turnStudy = input(
    'Que turno você estuda? Digite (M)- para Matutino, (V)- para Vespertino e (N)- para Noturno: ')

toLower = turnStudy.lower()

if toLower == "m":
    print("Bom dia!")
elif toLower == 'v':
    print('Boa tarde!')
elif toLower == "n":
    print("Boa noite!")
else:
    print('Valor inválido')
