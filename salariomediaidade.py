
soma_idade = 0
contagem_total = 0
soma_salarios = 0
contagem_acima_40 = 0
contagem_abaixo_2000 = 0


while True:
    try:
        idade = int(input("Digite a idade (ou um número negativo para encerrar): "))
        if idade < 0:
            break  
        
        salario = float(input("Digite o salário: R$"))
      
        if idade >= 0:
            soma_idade += idade
            contagem_total += 1
        
        if idade > 40:
            soma_salarios += salario
            contagem_acima_40 += 1
        
        if salario < 2000:
            contagem_abaixo_2000 += 1
    
    except ValueError:
        print("Valor inválido. Por favor, digite uma idade válida (número inteiro) e um salário válido (número decimal).")
if contagem_total > 0:
    media_idade = soma_idade / contagem_total
else:
    media_idade = 0
if contagem_acima_40 > 0:
    media_salarios_acima_40 = soma_salarios / contagem_acima_40
else:
    media_salarios_acima_40 = 0

print(f"Média de idade do grupo: {media_idade:.2f} anos")
print(f"Média de salários das pessoas com mais de 40 anos: R${media_salarios_acima_40:.2f}")
print(f"Quantidade de pessoas com salário abaixo de R$2000,00: {contagem_abaixo_2000}")
