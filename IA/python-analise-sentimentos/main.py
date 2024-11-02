from analise_sentimentos import AnaliseSentimentos
from googletrans import Translator

analise = AnaliseSentimentos()
translator = Translator()

frase = input("Digite uma frase: ")
translated = translator.translate(frase, dest='pt').text
# print(f"Frase traduzida: {translated}") # SE QUISER VER A FRASE TRADUZIDA PARA PORTUGUÊS

resultado = analise.avalia(translated)

if resultado['score'] > 0:
    print("A frase é positiva.")
elif resultado['score'] < 0:
    print("A frase é negativa.")
else:
    print("A frase é neutra.")

# O ARQUIVO TXT SÓ TINHA PALAVRAS EM PORTUGUÊS, ENTÃO, PREFERI TRADUZIR PARA O PORTUGUÊS E VALIDAR A FRASE.

# TESTEI O CÓDIGO COM AS SEGUINTES FRASES, NOS SEGUINTES IDIOMAS:
# Inglês: "I love to travel and explore new places."
# Espanhol: "La vida es hermosa y llena de sorpresas."
# Francês: "La situation actuelle est devenue anarchique et chaotique."
# Alemão: "Das Wetter ist heute sehr schön."
# Italiano: "Mi piace mangiare la pizza con gli amici."
# Japonês: "私は新しいことを学ぶのが好きです。"
# Chinês: "生活是美好的，每天都有新的可能。"
# Russo: "Я люблю читать книги на свежем воздухе."