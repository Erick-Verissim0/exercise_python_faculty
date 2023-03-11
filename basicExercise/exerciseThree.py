while True:
  numberOneDigited = int(input('Digite o primeiro valor numérico: '))
  numberTwoDigited = int(input('Digite o segundo valor numérico: '))

  totalDigited = numberOneDigited + numberTwoDigited

  requestContinuation = input('Você deseja continuar? Precione (y) para Sim e (n) para Não: ')

  print("A soma dos valores foi ", totalDigited)

  if requestContinuation != 'y':
    break

  print('----------------------------------')

print('----- Você saiu com sucesso! -----')
