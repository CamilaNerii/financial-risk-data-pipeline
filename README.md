# Financial Risk Data Pipeline

This project simulates an end-to-end data pipeline for a fintech, focusing on credit risk analysis. It covers the entire lifecycle of data: from raw ingestion to a structured Data Warehouse optimized for BI.

## 📁 Project Structure
- `data/`: Local storage for data files.
    - `raw/`: Original CSV files (Source).
    - `stage/`: Initial database for integrity checks (Staging Area).
    - `dw/`: Final modeled database (Data Warehouse) - *Not synced to GitHub for security*.
- `scripts/`: Python scripts for ETL automation.
- `dashboards/`: Power BI visualization files and templates.

## 🛠️ Tech Stack
- **Python (Pandas):** Data cleaning, standardization, and transformation.
- **SQLite:** Lightweight database used for Staging and Data Warehouse layers.
- **Power BI:** Data modeling (Star Schema) and executive dashboards.
- **Git/GitHub:** Version control and documentation.

## ⚙️ Data Pipeline Steps
- **Extraction:** Ingesting raw credit data from external sources (Kaggle).
- **Staging:** Loading data into a Staging Area to preserve the original source and allow auditing.
- **ETL & Modeling:** 
    - Handling missing values (e.g., `saving_accounts`).
    - Standardizing column names to `snake_case`.
    - Structuring data into **Fact** and **Dimension** tables (Star Schema).
- **Loading:** Exporting the cleaned data into the final Data Warehouse.
- **Visualization:** Creating KPIs for risk exposure and credit distribution.

---

## 🇧🇷 Versão em Português

Este projeto simula um pipeline de dados ponta a ponta para uma fintech, com foco em análise de risco de crédito. O projeto cobre todo o ciclo de vida dos dados: desde a ingestão bruta até um Data Warehouse estruturado e otimizado para BI.

### 📁 Estrutura do Projeto
- `data/`: Armazenamento local de dados.
    - `raw/`: Arquivos CSV originais (Fonte).
    - `stage/`: Banco de dados inicial para verificações de integridade (Staging Area).
    - `dw/`: Banco de dados final modelado (Data Warehouse) - *Não sincronizado com o GitHub por segurança*.
- `scripts/`: Scripts Python para automação do ETL.
- `dashboards/`: Arquivos de visualização do Power BI.

### 🛠️ Tecnologias Utilizadas
- **Python (Pandas):** Limpeza, padronização e transformação de dados.
- **SQLite:** Banco de dados para as camadas de Staging e Data Warehouse.
- **Power BI:** Modelagem de dados (Star Schema) e dashboards executivos.
- **Git/GitHub:** Controle de versão e documentação.

### ⚙️ Etapas do Pipeline
- **Extração:** Ingestão de dados brutos de crédito de fontes externas (Kaggle).
- **Staging:** Carga dos dados em uma Staging Area para preservar a fonte original e permitir auditoria.
- **ETL & Modelagem:** 
    - Tratamento de valores nulos (ex: `saving_accounts`).
    - Padronização de colunas para o formato `snake_case`.
    - Estruturação dos dados em tabelas **Fato** e **Dimensão** (Star Schema).
- **Carga (Load):** Exportação dos dados limpos para o Data Warehouse final.
- **Visualização:** Criação de KPIs de exposição de risco e distribuição de crédito.