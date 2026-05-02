

soma = float(0)
nome = str(input("Nome do Aluno?:"))
for i in range(1,4):
    print("Nota", i, "de 3")
    nota = float(input("Qual a nota?:"))
    soma = soma+nota
soma = soma/3

if soma > 7:
    print("Parabéns", nome, "Você foi aprovado.")
elif soma < 7 and soma > 5:
    print("Você ficou com média", soma, "e esta de recuperação")
else:
    print(nome,"você esta reprovado :(")        
