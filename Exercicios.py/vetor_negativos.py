matriz = [0]*4
for i in range(len(matriz)):
    matriz[i]= input(f"Digite valores para a matriz[{i}]: ")
    matriz[i] = int(matriz[i])  # Convertendo a entrada para inteiro
for i in range(len(matriz)):
    if matriz[i] >0:
        print(matriz[i])
    else:
        print()
