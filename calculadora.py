def adicao(num1, num2):
    return num1 + num2

def subtracao(num1, num2):
    return num1 - num2

def multiplicacao(num1, num2):
    return num1 * num2

def divisao(num1, num2):
    if num2 == 0:
        return "Erro: divisão por zero!"
    else:
        return num1 / num2

def main():
    print("Calculadora Básica")
    
    
    while True:
        try:
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
            
            print("Operações disponíveis:")
            print("1 - Adição (+)")
            print("2 - Subtração (-)")
            print("3 - Multiplicação (*)")
            print("4 - Divisão (/)")
            
            escolha = input("Escolha a operação (1/2/3/4): ")
            
            if escolha in ['1', '2', '3', '4']:
                if escolha == '1':
                    resultado = adicao(num1, num2)
                    operacao = "+"
                elif escolha == '2':
                    resultado = subtracao(num1, num2)
                    operacao = "-"
                elif escolha == '3':
                    resultado = multiplicacao(num1, num2)
                    operacao = "*"
                elif escolha == '4':
                    resultado = divisao(num1, num2)
                    if isinstance(resultado, str):  # Verifica se houve um erro na divisão
                        print(resultado)
                        continue  # Reinicia o loop sem imprimir o resultado da operação
                    else:
                        operacao = "/"
                
                print(f"Resultado: {num1} {operacao} {num2} = {resultado}")
                break  # Encerra o loop após a operação bem-sucedida
            else:
                print("Escolha inválida. Por favor, escolha uma operação válida (1/2/3/4).")
        except ValueError:
            print("Por favor, digite números válidos.")

if __name__ == "__main__":
    main()
