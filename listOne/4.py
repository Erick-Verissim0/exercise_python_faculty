# Mostrando se a media for maior que 7 aprovado e etc.

noteOne = int(input('Digite sua primeira nota: '))
noteTwo = int(input('Digite sua segunda nota: '))

result = (noteOne + noteTwo) / 2

if result > 6:
    print('Aprovado! Sua média foi ', result)
elif result < 7:
    print("Reprovado! Sua média foi ", result)
elif result == 10:
    print("Aprovado com Maestria! Sua média foi ", result)
