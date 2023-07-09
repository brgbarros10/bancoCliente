def menu():
  print('[S] - saque')
  print('[D] - depósito')
  print('[O] - saldo')
  print('[E] - extrato')
  print('[Q] - sair')
  return input()

def deposito(valor):
  global total_conta
  if valor<0:
    print('Valor negativo!\n')
    return valor
  else:
    historico.append(["Depósito:", valor])
    total_conta += valor
    return total_conta

def saldo():
  global total_conta
  print(f'Teu saldo atual é: R$ {total_conta}')

def saque(valor):
  global total_conta
  global numero_saque
  if numero_saque==LIMITE_SAQUE:
    print('Você já realizou os saques permitidos para hoje!\n')
  elif valor>500:
    print("Valor máximo para esta operação R$ 500,00\n")
  elif total_conta<=0:
    print("Saldo indisponível!\n")
  else:
    total_conta -= valor
    numero_saque += 1
    historico.append(['Saque', valor])

def extrato():
  if not historico:
    print('Não foram realizadas operações nesta conta! ')
  else:
    for i in historico:
      print(f'{i[0]} no valor de R$ {i[1]:.2f}')
    print(f'Total na conta: R$ {total_conta:.2f}\n')
    
total_conta = 0
historico = []
numero_saque = 0
LIMITE_SAQUE = 3

while True:
  opcao = menu()
  opcao = opcao.upper()
  if opcao == 'S':
     valor = float(input('Valor do saque: '))
     saque(valor)
  elif opcao == 'D':
     valor = float(input('Valor do deposito: '))
     deposito(valor)
  elif opcao == 'O':
    saldo()
  elif opcao == 'E':
    extrato()
  else:
    break
