#Escreva um algoritmo para calcular o valor final da mensalidade de uma academia com base na forma de pagamento escolhida pelo cliente.
#  O sistema deve solicitar o valor da mensalidade, apresentar as formas de pagamento disponíveis
#  (1 - Cartão sem desconto, 2 - Pix com 6% de desconto e 3 - Dinheiro com 10% de desconto), 
# solicitar a forma de pagamento escolhida, calcular e exibir o valor final da mensalidade e o desconto aplicado.#

mes = float(input("Qual sua mensalidade?: R$"))
print("*Qual a forma de pagamento?*")
forma = int(input("Cartão [1] Pix [2] Dinheiro [3] :"))
desconto = 0

if forma == 1:
    print("O valor a ser pago é de R$", mes)
elif forma == 2:
    desconto = (mes/100)*6
    mes = mes-desconto
    print("DESCONTO DE 6% NA SUA MENSALIDADE")
    print("O valor a ser pago é de R$", mes)
elif forma == 3:
    desconto = (mes/100)*10
    mes = mes-desconto
    print("DESCONTO DE 10% NA SUA MENSALIDADE")
    print("O valor a ser pago é de R$", mes)
else:
    print("Valor invalido :(")    
