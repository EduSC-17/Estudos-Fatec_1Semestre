#Escreva um algoritmo que receba dois valores (raio e altura) e calcule o valor do volume de uma lata de óleo.

raio = float(input("Qual o raio?: "))
altura = float(input("qual a altura?: "))

vol = (3.14*(raio*raio))*altura

print("O volume da sua lata é de:",vol)