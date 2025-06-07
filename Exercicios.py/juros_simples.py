print("Calculo de juros por ano")
p = float(input("Digite o valor do capital: R$ "))
i = float(input("Digite a taxa de juros mensais: "))
n = int(input("Digite o número de anos: "))
total = p+(p*i/100)*n*12
print(f"O total a pagar após {n} anos é: R$ {total:.2f}")