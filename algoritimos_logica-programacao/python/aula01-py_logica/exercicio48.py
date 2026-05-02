#Escreva um algoritmo que receba um nome e duas notas. Caso a média das notas seja maoir ou igual a 7, exiba a mensagem
# "Parabéns (nome)! Você foi aprovado". Caso contrário, exiba a mensagem "Você ficou com média (média) e foi reprovado".

nome = str(input("Nome do aluno:"))
n1 = float(input("1ª nota:"))
n2 = float(input("2ª nota:"))
med = n1+n2
res = med/2

if res >= 7:
    print("Parabéns", nome,"! Você foi aprovado")
else:
    print("Você foi reprovado, sua média foi", res)    