#Escreva um algoritmo que receba o valor de um produto e calcule um desconto de 10%,#
#exibindo para o usuário o valor do produto, o preço com desconto e quanto ele economizou.

produto = float(input("Qual o valor do produto?: "))
desconto = (produto/100)*10
prodes = produto-desconto

print("O valor do produto é de: R$",produto)
print("O valor do produto descontado é de: R$",prodes)
print("Você economizou R$",desconto,"!")