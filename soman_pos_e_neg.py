
while True:
    try:
        n = int(input("Digite um valor inteiro e positivo para n: "))
        if n > 0:
            break 
        else:
            print("Por favor, digite um valor inteiro e positivo.")

    except ValueError:
        print("Entrada inválida. Por favor, digite um número inteiro válido.")

S = 0.0

for i in range(1, n + 1):
    S += 1.0 / i 

print(f"A soma S = {S:.6f}")
