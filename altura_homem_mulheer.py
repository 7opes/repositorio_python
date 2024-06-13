
soma_altura_mulheres = 0.0
count_mulheres = 0
soma_altura_homens = 0.0
count_homens = 0

while True:
    sexo = input("Digite o sexo da pessoa (M para masculino, F para feminino, ou Enter para encerrar): ")
    
    if sexo == '': 
        break
    
    if sexo.upper() not in ['M', 'F']: 
        print("Sexo inválido. Digite M para masculino ou F para feminino.")
        continue
    
    try:
        altura = float(input("Digite a altura da pessoa em metros: "))
        
        if sexo.upper() == 'F':
            soma_altura_mulheres += altura
            count_mulheres += 1
        elif sexo.upper() == 'M':
            soma_altura_homens += altura
            count_homens += 1
    
    except ValueError:
        print("Altura inválida. Digite um número válido para a altura.")


if count_mulheres > 0:
    media_altura_mulheres = soma_altura_mulheres / count_mulheres
else:
    media_altura_mulheres = 0.0 
if count_homens > 0:
    media_altura_homens = soma_altura_homens / count_homens
else:
    media_altura_homens = 0.0  

print(f"Altura média das mulheres: {media_altura_mulheres:.2f} metros")
print(f"Altura média dos homens: {media_altura_homens:.2f} metros")
