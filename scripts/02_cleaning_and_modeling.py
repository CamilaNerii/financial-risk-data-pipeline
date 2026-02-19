import pandas as pd
import sqlite3
import os

# --- CONFIGURAÇÃO ---
PATH_STG = 'data/stage/financial_stg.db'
PATH_DW = 'data/dw/financial_dw.db'
os.makedirs('data/dw', exist_ok=True)

# --- LEITURA ---
conn_stg = sqlite3.connect(PATH_STG)
df = pd.read_sql('SELECT * FROM stg_german_credit', conn_stg)
conn_stg.close()

# --- DICIONÁRIO DE TRADUÇÃO (Mapeamento) ---

traducao = {
    'alter': 'age',
    'hoehe': 'credit_amount',
    'laufzeit': 'duration',
    'sparkont': 'saving_accounts',
    'beruf': 'job',
    'wohn': 'housing',
    'pers': 'sex', 
    'verw': 'purpose',
    'kredit': 'risk'
}

# Aplicando a tradução
df = df.rename(columns=traducao)

# --- LIMPEZA ---

if 'saving_accounts' in df.columns:
    df['saving_accounts'] = df['saving_accounts'].fillna('Unknown')

# --- MODELAGEM STAR SCHEMA ---
print("📐 Estruturando Star Schema")

# Colunas para a Dimensão Cliente 
cols_cliente = ['age', 'sex', 'job', 'housing']

d_customer = df[cols_cliente].drop_duplicates().reset_index(drop=True)
d_customer['customer_id'] = d_customer.index + 1

f_credit = df.merge(d_customer, on=cols_cliente)
f_credit = f_credit[['customer_id', 'credit_amount', 'duration', 'purpose', 'risk']]

# --- CARGA NO DATA WAREHOUSE ---
conn_dw = sqlite3.connect(PATH_DW)
d_customer.to_sql('dim_customer', conn_dw, if_exists='replace', index=False)
f_credit.to_sql('fact_credit', conn_dw, if_exists='replace', index=False)
conn_dw.close()

print("✅ SUCESSO! O Data Warehouse foi criado com os dados traduzidos.")