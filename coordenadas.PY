import math
xl = float(input("Valor de xl (coordenada x de P1): "))
y1 = float(input("Valor de y1 (coordenada y de P1): "))
x2 = float(input("Valor de x2 (coordenada x de P2): "))
y2 = float(input("Valor de y2 (coordenada y de P2): "))
distancia = math.sqrt((x2 - xl)**2 + (y2 - y1)**2)

print(f"A distância P1({xl}, {y1}) e P2({x2}, {y2}) é: {distancia}")
