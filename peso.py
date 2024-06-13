def calcular_peso_ideal(altura, sexo):
    if sexo.upper() == 'M':
        peso_ideal = (72.7 * altura) - 58
    elif sexo.upper() == 'F':
        peso_ideal = (62.1 * altura) - 44.7
    else:
        return None 
    
    return peso_ideal

while True:
    try:
        altura = float(input("Digite sua altura em metros (ou 0 para sair): "))
        if altura == 0:
            break  
        
        sexo = input("Digite seu sexo (M para Masculino, F para Feminino): ")

        if sexo.upper() not in ['M', 'F']:
            print("Sexo inválido. Por favor, digite M para Masculino ou F para Feminino.")
            continue 
        
        peso_ideal = calcular_peso_ideal(altura, sexo)
        
        if peso_ideal is not None:
            print(f"Seu peso ideal é: {peso_ideal:.2f} kg")
        else:
            print("Erro ao calcular o peso ideal. Verifique as entradas.")
    
    except ValueError:
        print("Entrada inválida. Por favor, digite uma altura válida (número decimal).")

print("Programa encerrado.")
