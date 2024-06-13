def verificar_votacao(idade):
    if idade < 16:
        return "Não eleitor (idade menor que 16 anos)"
    elif 16 <= idade < 18 or idade >= 65:
        return "Eleitor facultativo (idade entre 16 e 18 anos ou idade igual ou superior a 65 anos)"
    else:  # idade >= 18 e idade < 65
        return "Voto obrigatório (idade entre 18 e 65 anos)"

def main():
    while True:
        try:
            entrada = input("Digite a idade da pessoa (ou 'sair' para terminar): ")
            if entrada.lower() == 'sair':
                print("Programa encerrado.")
                break
            idade = int(entrada)
            if idade < 0:
                print("Por favor, digite uma idade válida maior ou igual a zero.")
                continue
            situacao_votacao = verificar_votacao(idade)
            print(f"Situação de votação: {situacao_votacao}")
        except ValueError:
            print("Por favor, digite uma idade válida (número inteiro) ou 'sair' para terminar.")

if __name__ == "__main__":
    main()
