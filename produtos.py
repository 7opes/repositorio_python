def calcular_valor_venda(nome_produto, valor_compra):
    if valor_compra < 10.00:
        lucro_percentual = 0.70  # Lucro de 70%
    elif 10.00 <= valor_compra < 30.00:
        lucro_percentual = 0.50  # Lucro de 50%
    elif 30.00 <= valor_compra < 50.00:
        lucro_percentual = 0.40  # Lucro de 40%
    else:
        lucro_percentual = 0.30  # Lucro de 30%
    
    valor_lucro = valor_compra * lucro_percentual
    valor_venda = valor_compra + valor_lucro
    
    print(f"Nome do Produto: {nome_produto}")
    print(f"Valor de Compra: R${valor_compra:.2f}")
    print(f"Lucro ({lucro_percentual*100:.0f}%): R${valor_lucro:.2f}")
    print(f"Valor de Venda: R${valor_venda:.2f}")

def main():
    print("Calculadora de Valor de Venda")
    print("=============================")
    
    nome_produto = input("Digite o nome do produto: ")
    
    while True:
        try:
            valor_compra = float(input("Digite o valor de compra (R$): "))
            if valor_compra <= 0:
                print("O valor de compra deve ser maior que zero.")
            else:
                calcular_valor_venda(nome_produto, valor_compra)
                break
        except ValueError:
            print("Por favor, digite um valor de compra válido (número real).")

if __name__ == "__main__":
    main()
