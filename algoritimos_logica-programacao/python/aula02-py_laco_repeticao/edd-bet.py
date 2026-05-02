import random
##importa uma biblioteca para gerar números aleatórios
print("--------------------")
print("    EddBet 2000     ")
print("--------------------")

segredo = random.randrange(1,11)
#print(segredo, "Foi sorteado")

acertou = False
tentativas = 3
i = 1

while i<=3:
    i +=1
    print("Você possui", tentativas, "tentativas de 3/n")
    numero = int(input("Digite um número entre 1 a 10:"))

    if numero >10 or numero < 0:
        print("é de 1 a 10 mula, tenta denovo")
        i -= 1      
        tentativas += 1
    if numero == segredo:
        acertou = True      
    if acertou:
        print("----------------------------------------")
        print(    "VOCÊ ACERTOU!!! GANHOU R$0.10!!!")      
        print("----------------------------------------")
        break
    else:   
        print("Você errou, perdeu R$1.00 :(")
        tentativas -= 1