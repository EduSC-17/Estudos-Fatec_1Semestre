#Escreva um algoritmo que verifique se uma letra digitada é vogal ou consoante.

letra = str(input("Digite uma letra minuscula: "))

if letra == 'a' or letra == 'e' or letra == 'i' or letra == 'o' or letra == 'u':
    print("Vogal")
else:
    print("Consoante")    