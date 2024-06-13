mes = input("Qual mês da viagem? (1 a 12):")
quantidade_passagens = int(input("Quantas passagens deseja?: "))

if quantidade_passagens <= 0:
    print("Informe a qauntidade!!!.")
else:
    
    if mes in ['2', '3', '4', '5']:
        valor_por_passagem = 350.99
    elif mes in ['1', '6', '7', '12']:
        valor_por_passagem = 520.50
    elif mes in ['8', '9', '10', '11']:
        valor_por_passagem = 450.75
    else:
        print("Mês inválido.")
        exit()
        
    valor_total = quantidade_passagens * valor_por_passagem
    
    mensagem = "O valor total a pagar pelas " + str(quantidade_passagens) + " passagens é: R$" + format(valor_total, ".2f")
    print(mensagem)