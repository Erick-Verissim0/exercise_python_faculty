# Ver se a letra digitada é vogal ou consoante

insertLetter = input('Digite uma letra: ')

toLower = insertLetter.lower()

if toLower in 'aeiou':
    print('É vogal!')
else:
    print('É consoante!')
