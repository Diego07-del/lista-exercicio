a,l = input("Digite a base e a altura do retângulo, dê um espaço entre as informaçoes: ").split()
a = float(a)  # Convertendo a base para float
l = float(l)  # Convertendo a altura para float
area = a * l
print(f"A área do retângulo é: {area:.2f} m²")