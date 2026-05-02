#Escreva um algoritmo para efetuar o cálculo do reajuste de salário de um funcionário.
#  Considere que o funcionário deve receber um reajuste de 15% caso seu salário seja menor de 500.
#  Se o salário for maior ou igual a 500, mas menor ou igual a 1000, seu reajuste será de 10%;
#  caso seja maior de 1000 o reajuste deverá ser de 5%.#

salario = float(input("Qual seu salario?: R$"))

if salario > 0 and salario < 500:
    quinze = (salario/100)*15
    salnovo = salario-quinze
    print("seu novo salario é de: R$", salnovo)
elif salario >=500 and salario <=1000:
    dez = (salario/100)*10
    salnovo = salario-dez
    print("seu novo salario é de: R$", salnovo)
elif salario >1000:
    cinco = (salario/100)*5
    salnovo = salario-cinco
    print("seu novo salario é de: R$", salnovo)
else:
    print("Valor invalido")