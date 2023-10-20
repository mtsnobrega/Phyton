#sistema simples de uma calculadora 

num1 = float(input('Digite um numero: '))

Operação = input('Digite o sinal corresponde a operação que desaja calcular: (Adição +), (Subtração -), (multiplicação *) ou (Divisão /).')

num2 = float(input('Digite outro numero: '))

if Operação == '+':
  resultado = num1 + num2
  print('O resultado é: ', resultado)

elif Operação == '-':
  resultado = num1 - num2
  print('O resultado é: ', resultado)

elif Operação == '*':
  resultado = num1 * num2
  print('O resultado é ', resultado)

elif Operação == '/':
  if num2 != 0:
    resultado = num1 / num2
    print('O resultado é ', resultado)
  else:
    print('Não é possivel dividir por zero')
else:
  print('Ops... a operação definida é invalida')