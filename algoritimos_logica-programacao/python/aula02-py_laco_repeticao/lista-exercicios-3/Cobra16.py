

contn = int(input("Quantas notas quer colocar?: "))
soma = 0
contador = contn + 1
for i in range(1,contador,1):
    print("Nota", i, "de",contn)
    nota = float(input("Qual a nota?:"))
    soma = soma+nota
soma = soma/contn    
print(soma)