from peewee import *
import csv
import os

# Definindo o banco de dados SQLite
db = SqliteDatabase('banco_teste.db')

# Modelo para armazenar as informações da companhia
class CNPJ(Model):
    cnpj = CharField(unique=True)
    denom_social = CharField()
    sit = CharField()

    class Meta:
        database = db  # Ligando o modelo ao banco de dados

# Criando as tabelas no banco de dados (se não existirem)
db.connect()
db.create_tables([CNPJ])

# Função para importar dados do arquivo CSV
def importar_dados_csv(arquivo_teste):
    if os.path.exists(arquivo_teste):
        with open(arquivo_teste, 'r', newline='', encoding='utf-8') as arquivo_teste:
            leitor_csv = csv.DictReader(arquivo_teste)
            for linha in leitor_csv:
                cnpj_cia = linha.get('CNPJ_CIA')
                denom_social = linha.get('DENOM_SOCIAL')
                sit = linha.get('SIT')
                # Verifica se os campos obrigatórios existem na linha
                if cnpj_cia and denom_social and sit:
                    # Insere na tabela CNPJ
                    CNPJ.create(cnpj=cnpj_cia, denom_social=denom_social, sit=sit)
                    print(f"Dados inseridos: CNPJ: {cnpj_cia}, Denominação Social: {denom_social}, Situação: {sit}")
                else:
                    print("Registro incompleto, pulando...")
    else:
        print(f"Arquivo '{arquivo_teste}' não encontrado.")

# Chamando a função para importar dados do arquivo CSV (substitua 'arquivo.csv' pelo caminho absoluto do seu arquivo)
importar_dados_csv('C:\\Users\\Vitor\\OneDrive\\Documentos\\testevaga\\arquivo_teste.csv')

# Exemplo de consulta no banco de dados
for cnpj in CNPJ.select().where(CNPJ.sit == 'ATIVO'):
    print(f"CNPJ: {cnpj.cnpj}, Denominação Social: {cnpj.denom_social}, Situação: {cnpj.sit}")
