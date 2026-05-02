#Escreva um programa que recebe o preço de dois produtos.
#Calcule um desconto de 8% no 1º produto, 11% no 2º e apresente o valor final a ser pago.

pro1 = float(input("Produto 1:"))
pro2 = float(input("Produto 2:"))
des1 = (pro1/100)*8
des2 = (pro2/100)*11
nov1 = (pro1-des1)+(pro2-des2)
print("vai ter que pagar: R$",nov1)