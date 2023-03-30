name = input('Digite seu nome: ')

regex = '[aeiouAEIOU]'

quantity = 0

for letter in name:
    if letter in regex:
        quantity += 1

print(quantity)
