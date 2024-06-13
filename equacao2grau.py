import math

def calcular_raizes(a, b, c):
    if a == 0:
        print("Isso não é uma equação de segundo grau (a = 0).")
        return
    
    # Calculando o discriminante delta
    delta = b**2 - 4*a*c
    
    if delta > 0:
        # Duas raízes reais distintas
        raiz1 = (-b + math.isqrt(delta)) / (2*a)
        raiz2 = (-b - math.isqrt(delta)) / (2*a)
        print(f"As raízes da equação são: {raiz1} e {raiz2}")
    elif delta == 0:
        # Uma raiz real (raíz dupla)
        raiz = -b / (2*a)
        print(f"A equação possui uma raiz dupla: {raiz}")
    else:
        # Delta negativo, sem raízes reais
        print("A equação não possui raízes reais (delta negativo).")

def main():
    while True:
        try:
            # Entrada dos coeficientes da equação como inteiros
            a = int(input("Digite o coeficiente a (inteiro): "))
            b = int(input("Digite o coeficiente b (inteiro): "))
            c = int(input("Digite o coeficiente c (inteiro): "))
            
            # Chamando a função para calcular as raízes
            calcular_raizes(a, b, c)
            break  # Encerra o loop após o cálculo bem-sucedido
        except ValueError:
            print("Por favor, digite coeficientes válidos (números inteiros).")

if __name__ == "__main__":
    print("Este programa calcula as raízes de uma equação de segundo grau (ax^2 + bx + c = 0) com coeficientes inteiros.")
    main()
