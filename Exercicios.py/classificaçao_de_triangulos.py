a = int(input("Digite o primeiro lado do triângulo: "))
b= int(input("Digite o segundo lado do triângulo: "))
c = int(input("Digite o terceiro lado do triângulo: "))
if a == b and b == c:
    print("O triângulo é equilátero.")
elif a == b or b ==c or c == a:
    print("O triângulo é isósceles.")
elif a & b and b &c or c& a:
    print("O triângulo é escaleno.")