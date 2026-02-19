import pandas as pd
import sqlite3
import os

# Caminhos (Onde o arquivo está e para onde vai)
PATH_RAW = 'data/raw/german_credit_data.csv'
PATH_STG = 'data/stage/financial_stg.db'

# Garante que a pasta 'stage' exista
os.makedirs('data/stage', exist_ok=True)

print("⏳ Iniciando Passo 01: Extração e Carga na Staging Area...")

# 1. Tenta ler o arquivo que você salvou na RAW
try:
    df = pd.read_csv(PATH_RAW, index_col=0)
    
    # 2. Conecta ao banco de dados da Staging Area (Cria o arquivo se não existir)
    conn = sqlite3.connect(PATH_STG)
    
    # 3. Salva os dados brutos como uma tabela chamada 'stg_german_credit'
    df.to_sql('stg_german_credit', conn, if_exists='replace', index=False)
    
    conn.close()
    print("✅ Sucesso! O dado bruto agora está salvo em data/stage/financial_stg.db")

except FileNotFoundError:
    print("❌ Erro: O arquivo CSV não foi encontrado na pasta data/raw/. Verifique o nome do arquivo!")