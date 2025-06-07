print("calculo de IMC ")
p = float(input("Digite seu peso em kg:"))
a = float(input("Digite sua altura em centimetros:"))
a =(a*0.1)
imc = p / (a *a)
imc = imc * 100
print(f"seu imc é:{imc:.2f}")
if imc < 18.5:
    print("Abaixo do peso")
elif imc < 24.9:
    print("Peso normal")
elif imc < 29.9:
    print("Sobrepeso")  
elif imc < 34.9:
    print("Obesidade grau 1")
elif imc < 39.9:
    print("Obesidade grau 2")
else:
    print("Obesidao")
