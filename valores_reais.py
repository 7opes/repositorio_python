count_positivos = 0
count_negativos = 0


menor_valor = float('inf')  


while True:
    try:
        valor_str = input("Digite um valor real (ou pressione Enter para encerrar): ")
        
        if valor_str == '': 
            break
        
        valor = float(valor_str)  
        
        if valor > 0:
            count_positivos += 1
        elif valor < 0:
            count_negativos += 1
        
        if valor < menor_valor:
            menor_valor = valor
    
    except ValueError:
        print("Entrada inválida. Por favor, digite um valor numérico.")

# Imprimir resultados
print(f"Quantidade de valores positivos: {count_positivos}")
print(f"Quantidade de valores negativos: {count_negativos}")

if count_positivos + count_negativos > 0:
    print(f"Menor valor encontrado: {menor_valor}")
else:
    print("Nenhum valor foi inserido.")
