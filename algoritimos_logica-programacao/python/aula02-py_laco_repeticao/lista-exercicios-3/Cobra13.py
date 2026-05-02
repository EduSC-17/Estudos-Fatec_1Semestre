

produto = float(input("Qual o valor do produto?: R$"))
parcela = float(input("Quantas parcelas?:"))

juros = (produto/100)*7
produto = (produto+juros)/parcela
total = produto*parcela

print("Você vai pagar", parcela, "parcelas de", produto)
print("O valor da compra ficou: R$", total)