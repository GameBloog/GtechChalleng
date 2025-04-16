# 📊 Análise dos 5 Principais Países Importadores de Carne

O objetivo deste projeto é ilustrar os cinco principais países que mais importam carne, de acordo com os valores de importação. A ideia original era executar a consulta diretamente no **BigQuery**, utilizando o banco de dados público **base dos dados**.

## ☁️ Tentativa de uso do BigQuery

Um trecho de código foi utilizado para consultar via **BigQuery**, conforme abaixo:

```python
import pandas_gbq

project_id = "basedosdados.br_trase_supply_chain.beef"

query = """
SELECT
    country_first_import_name AS pais,
    SUM(fob_usd) AS valor_total_importacao
FROM basedosdados.br_trase_supply_chain.beef
WHERE
    year = (SELECT MAX(year) FROM basedosdados.br_trase_supply_chain.beef)
GROUP BY country_first_import_name
ORDER BY valor_total_importacao DESC
LIMIT 5;
"""
```

Ao executar a consulta, tive problemas de permissão com o projeto/conjunto de dados do BigQuery. Como não consegui alterar as permissões, utilizei uma matriz de dados simulada para ilustrar.

## 🧪 Uso de dados simulados (mock data)

Os dados foram inseridos no código para simular a saída esperada.

```python
dados_importacao = [
    {"pais": "CHINA (HONG KONG)", "valor_total_importacao": 1296082440.0},
    {"pais": "CHINA (MAINLAND)", "valor_total_importacao": 929010115.0},
    {"pais": "IRAN", "valor_total_importacao": 547464424.0},
    {"pais": "EGYPT", "valor_total_importacao": 526967591.0},
    {"pais": "RUSSIAN FEDERATION", "valor_total_importacao": 462655593.0}
]
```
"
Essas informações permitiram o fluxo normal da análise, como processamento e exportação para o Excel.

## 🧼 Tratamento e formatação

Após o carregamento dos dados no DataFrame, foi feito:

- Tratamento de valores nulos (se houver)
- Formatação dos valores de importação em milhões de dólares

```python
df['valor_total_importacao_formatado'] = df['valor_total_importacao'].apply(
    lambda x: f"${x/1_000_000:.2f} million"
)
```

## 📁 Exportação para Excel

O resultado foi exportado para um arquivo `.xlsx` com formatação:

- Cabeçalhos com cor de fundo
- Colunas centralizadas
- Formatação de moeda

```python
with pd.ExcelWriter('top5PaisesImportadoresCarne.xlsx', engine='xlsxwriter') as writer:
    df.to_excel(writer, index=False, sheet_name='Top 5')

```

## ✅ Resultado

O arquivo gerado foi:

```
top5PaisesImportadoresCarne.xlsx
```

Ele contém os cinco principais países importadores de carne, com os respectivos valores totais de importação.
