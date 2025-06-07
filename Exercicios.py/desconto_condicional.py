desconto = 10
p = float(input("Digite o preço do produto: "))
if p <100:
    print("O produto não tem desconto.")
elif p >= 100:
    n = (p*desconto)/100
    p = p - n
    print(f"O produto tem desconto de {desconto}%, o novo preço é: {p:.2f}")