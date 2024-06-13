
count_votantes = 0
soma_idades_nao_votantes = 0

for i in range(5):  
    idade = int(input(f"Digite a idade do aluno {i+1}: "))

    if idade >= 16:  
        count_votantes += 1 
    else:
        soma_idades_nao_votantes += idade 

if count_votantes < 5: 
    media_idade_nao_votantes = soma_idades_nao_votantes / (5 - count_votantes)
else:
    media_idade_nao_votantes = 0  

print(f"Quantidade de alunos que podem votar: {count_votantes}")
print(f"Média da idade dos alunos que não podem votar: {media_idade_nao_votantes:.2f}")
