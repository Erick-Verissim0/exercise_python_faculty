import spacy

class AnaliseSentimentos: 

    """ 
        Classe para Realizar Análise de Sentimentos
    """ 
    def __init__(self):
        self.__nlp = spacy.load('pt_core_news_sm')
        self.__dicionario = {}
        self.__criaDicionario()

    def __criaDicionario(self):
        with open('./lexico.txt', 'r') as arquivo:
            linhas = arquivo.readlines()

        for linha in linhas:
            linha = linha.strip()
            if linha.startswith('#'):
                continue
            dado = linha.split(',')
            self.__dicionario[dado[0]] = int(dado[2])

    def avalia(self, texto):
        retorno = {'score': 0, 'entidades': []}
        
        tokens = self.__nlp(texto)

        retorno['entidades'] = tokens.ents

        for token in tokens:
            palavra = str(token.text).lower()

            if palavra in self.__dicionario:
                print('---------------------------------')
                retorno['score'] += self.__dicionario[palavra]
                print(f'Palavra encontrada: {palavra}')

        return retorno
