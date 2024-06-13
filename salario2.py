# Solicita ao usuário o turno de trabalho e a quantidade de horas trabalhadas
turno = input("Digite o turno de trabalho (N para Noturno ou D para Diurno): ")
quantidade_horas = float(input("Digite a quantidade de horas trabalhadas: "))

# Define o valor da hora de acordo com o turno de trabalho
if turno.upper() == "N":
    valor_hora = 45.00
else:
    valor_hora = 37.50

# Calcula o salário
salario = valor_hora * quantidade_horas

# Mostra o valor do salário
print("O salário é R$", salario)
