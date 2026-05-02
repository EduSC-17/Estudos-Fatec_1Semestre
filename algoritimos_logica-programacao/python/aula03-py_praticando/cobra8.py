#Escreva um algoritmo que receba 10 valores digitados pelo usuário
# e no final exiba a média dos números (utilize laço de repetição).

cont = 1
soma = 0
while cont <=10:
    print("Numero",cont,"de 10")
    num = float(input("Digite um numero: "))
    cont = cont + 1
    soma = soma + num

div = soma / 10
print("A média desses numeros é de", div)

