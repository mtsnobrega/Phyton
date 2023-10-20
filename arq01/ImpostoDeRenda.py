# sistema simples para calcular o imposto de renda sobre o salário e retornar o valor correspondente ao calculo de desconto do Imposto de renda e se caso ouver outro desconto pendente apresentar já debitado no valor final do salário

while True:
    num=input("Qual e a sua renda? R$")
    if num.isdigit():
      renda = int(num)
      break
    elif num.replace(".","",1).isdigit():
      renda = float(num)
      break 
    else:
      print("Insira um numero valido")
while True:
  duvida=input("Teria mais algum desconto? sim ou nao ")
  
  if duvida.lower() == "sim":
    x = input("Qual seria o valor do desconto? R$ ")
    if x.isdigit():
      desconto2=int(x)
      break
    elif x.replace(".","").isdigit():
      desconto2=float(x)
      break
    else:
      print("Digite apenas numeros")
  elif duvida.lower() == "nao":
    desconto2=0
    break
  else:
      print("Responda atentamente, sim ou nao");


rendafinal=renda-desconto2

if renda >= 0 and renda <= 2000.00:
  print("Você está isento do imposto de renda, e seu salário é R$" ,rendafinal)
elif (renda >=2000.01 and renda <=3000.00):
  print("A porcentagem de imposto, referente ao seu salario é de 8%")
  desconto=renda *0.08
  print("O valor de imposto descontado é", desconto);
  print("Salario com o desconto é ", rendafinal-desconto)
elif (renda >=3000.01 and renda <=4500.00):
    print("A porcentagem referente ao seu salário é de 18% ")
    desconto=rendafinal*0.18
    print("O valor de imposto descontado é",desconto)
    print("Salario com o desconto é ", rendafinal-desconto)
elif(renda >=4500):
    print("A porcentagem referente ao seu salário é de 28%")
    desconto=rendafinal*0.28
    print("O valor de imposto descontado é", desconto);
    print("Salario com o desconto é ", rendafinal-desconto);
else:
    print("Erro no sistema");
