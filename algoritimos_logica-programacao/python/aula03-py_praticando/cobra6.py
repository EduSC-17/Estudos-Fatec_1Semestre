peso = float(input("Qual o seu peso?: KG "))
altura = float(input("Qual a sua altura? Metros "))

imc = (peso/(altura*altura))

if imc <= 18.5 and imc >= 0:
    print("Abaixo do normal")
elif imc > 18.5 and imc <= 24.9:
    print("Normal")
elif imc > 25.0 and imc <= 29.9:
    print("Excesso de peso")
elif imc > 30.0 and imc <= 34.9:
    print("Obesidade nivel 1")
elif imc > 35.0 and imc <= 39.9:
    print("Obesidade nivel 2")
elif imc > 40.0:
    print("Obesidade nivel 3")
else:
    print("Valor invalido")

print("Seu IMC é de:", imc)