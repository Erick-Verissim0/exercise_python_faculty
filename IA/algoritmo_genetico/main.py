from ag import AlgoritmoGenetico

dados = [12.53, -33.12, 50.78, -78.99, 25.48, -60.83, 81.81, -20.55, 35.63, -40.51]

saveFitness = []

def funFitness(genes, dados):
    sumPression = 0

    for i in range(len(genes)):
        sumPression += genes[i] * dados[i]

    # print('saveFitness', saveFitness) Para ver todas as válvulas

    if 45.28 <= sumPression <= 48.33:
        saveFitness.append(sumPression)
        # print('sumPression', sumPression) Para ver somente a válvula
        return sumPression
    else:
        return 0

ag = AlgoritmoGenetico(dados,funcaoFitness=funFitness)
ag.executa()
print(ag.populacao)