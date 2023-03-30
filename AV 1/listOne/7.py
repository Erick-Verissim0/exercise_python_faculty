questionOne = str(input('Telefonou para a vitima? (S/N): '))
questionTwo = str(input('Esteve no local do crime? (S/N): '))
questionThree = str(input('Mora perto da vítima? (S/N): '))
questionFor = str(input('Devia para a vítima? (S/N): '))
questionFive = str(input('Quem trabalhou para a vítima? (S/N): '))

totalS = 0

if questionOne.lower() == "s":
    totalS += 1
if questionTwo.lower() == "s":
    totalS += 1
if questionThree.lower() == "s":
    totalS += 1
if questionFor.lower() == "s":
    totalS += 1
if questionFive.lower() == "s":
    totalS += 1


if totalS == 2:
    print("Você é considerado(a) suspeito(a)!")
elif totalS >= 3 and totalS <= 4:
    print("Você é considerado(a) cúmplice!")
elif totalS == 5:
    print("Você é considerado(a) assassino(a)!")
else:
    print("Você é considerado(a) inocente!")
