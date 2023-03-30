# Dizendo se o número digitado é par ou ímpar

numberDigited = int(input('Digite um número inteiro: '))

numberDivided = numberDigited % 2

if numberDivided == 0:
    print("O número que você digitou é PAR!")
else:
    print("O número que você digitou é IMPAR!")
