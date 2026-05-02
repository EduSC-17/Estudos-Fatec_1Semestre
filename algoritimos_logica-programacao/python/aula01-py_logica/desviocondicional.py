# desvio condicional varias opções a um tipo de resposta
aluno = str(input("é Aluno? [s/n]: "))
if aluno == 's':
    print("Bem-vindo aluno")
elif aluno == 'n':
    print("Bem-vindo convidado")
else:
    print("Opção Inválida")

print("Programa encerrados")