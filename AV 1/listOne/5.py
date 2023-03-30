numberOne = int(input('Digite um número: '))
numbertwo = int(input('Digite outro número: '))
numberThree = int(input('Digite novamente outro número: '))

if numberOne > numbertwo and numberOne > numberThree:
    print('O maior número é: ', numberOne)
elif numbertwo > numberThree and numbertwo > numberOne:
    print('O maior número é: ', numbertwo)
else:
    print('O maior número é: ', numberThree)
