#Escreva um algoritmo que receba três notas. Caso a média das notas seja maior ou igual a 7,
#  exiba a mensagem “Parabéns! Você foi aprovado”. Caso contrário, exiba a mensagem “Você foi reprovado”.#

n1 = float(input("1ª Nota:"))
n2 = float(input("3ª Nota:"))
n3 = float(input("3ª Nota:"))

media = (n1+n2+n3)/3

if media >= 7:
    print("Parabéns! Você foi aprovado.")
else:
    print("Você foi reprovado")
