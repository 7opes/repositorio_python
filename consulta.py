import csv

with open(r'C:\\Users\\Vitor\\OneDrive\\Documentos\\testevaga\\arquivo_teste.csv', mode='r', encoding='utf-8') as arquivo_teste:
    leitor_csv = csv.DictReader(arquivo_teste)
    for linha in leitor_csv:
       denom_social = linha['DENOM_SOCIAL']
print(denom_social)


"C:\Users\Vitor\teste_vaga\arquivo_teste.csv"