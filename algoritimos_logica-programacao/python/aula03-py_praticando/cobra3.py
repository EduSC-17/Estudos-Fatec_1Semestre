#Escreva um algoritmo que leia 3 notas de um aluno e calcule a média final considerando que a média é ponderada,
#  ou seja, o peso das notas são 2, 3 e 5.#

n1 = float(input("1ª Nota: "))
n2 = float(input("2ª Nota: "))
n3 = float(input("3ª Nota: "))

media = ((n1*2)+(n2*3)+(n3*5)) / (2+3+5)

print(media)