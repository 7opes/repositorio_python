def bin_to_decimal(binary):
    """Converte um número binário para decimal."""
    return int(binary, 2)

def decimal_to_binary(decimal):
    """Converte um número decimal para binário."""
    return bin(decimal)[2:]

def decimal_to_hexadecimal(decimal):
    """Converte um número decimal para hexadecimal."""
    return hex(decimal)[2:].upper()

def binary_addition(bin1, bin2):
    """Realiza a adição binária de dois números binários."""
    return bin(int(bin1, 2) + int(bin2, 2))[2:]

def binary_multiplication(bin1, bin2):
    """Realiza a multiplicação binária de dois números binários."""
    return bin(int(bin1, 2) * int(bin2, 2))[2:]

def display_menu():
    """Exibe o menu de opções."""
    print("\nMenu:")
    print("1. Converter número decimal para binário")
    print("2. Converter número decimal para hexadecimal")
    print("3. Converter número binário para decimal")
    print("4. Somar dois números binários")
    print("5. Multiplicar dois números binários")
    print("0. Sair")

def main():
    while True:
        display_menu()
        choice = input("Escolha a função desejada (0-5): ")

        if choice == '0':
            print("Programa encerrado.")
            break
        elif choice == '1':
            decimal = int(input("Digite um número decimal: "))
            print(f"Binário: {decimal_to_binary(decimal)}")
        elif choice == '2':
            decimal = int(input("Digite um número decimal: "))
            print(f"Hexadecimal: {decimal_to_hexadecimal(decimal)}")
        elif choice == '3':
            binary = input("Digite um número binário: ")
            print(f"Decimal: {bin_to_decimal(binary)}")
        elif choice == '4':
            binary1 = input("Digite o primeiro número binário: ")
            binary2 = input("Digite o segundo número binário: ")
            print(f"Soma binária: {binary_addition(binary1, binary2)}")
        elif choice == '5':
            binary1 = input("Digite o primeiro número binário: ")
            binary2 = input("Digite o segundo número binário: ")
            print(f"Multiplicação binária: {binary_multiplication(binary1, binary2)}")
        else:
            print("Opção inválida. Escolha novamente.")

if __name__ == "__main__":
    main()
