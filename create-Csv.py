import pandas as pd

dados_importacao = [
    {"pais": "CHINA (HONG KONG)", "valor_total_importacao": 1296082440.0},
    {"pais": "CHINA (MAINLAND)", "valor_total_importacao": 929010115.0},
    {"pais": "IRAN", "valor_total_importacao": 547464424.0},
    {"pais": "EGYPT", "valor_total_importacao": 526967591.0},
    {"pais": "RUSSIAN FEDERATION", "valor_total_importacao": 462655593.0}
]

df = pd.DataFrame(dados_importacao)

print("\nNull values ​​before treatment:")
print(df.isnull().sum())

df['valor_total_importacao'] = df['valor_total_importacao'].fillna(df['valor_total_importacao'].mean())
df['pais'] = df['pais'].fillna('Not informed')

print("\nNull values ​​after treatment:")
print(df.isnull().sum())

df['valor_total_importacao_formatado'] = df['valor_total_importacao'].apply(
    lambda x: f"${x/1_000_000:.2f} million"
)

print("\nResulting DataFrame:")
print(df)

excel_file = 'top5PaisesImportadoresCarne.xlsx'

with pd.ExcelWriter(excel_file, engine='xlsxwriter') as writer:
    df.to_excel(writer, index=False, sheet_name='Top 5')

    workbook = writer.book
    worksheet = writer.sheets['Top 5']

    header_format = workbook.add_format({
        'bold': True, 'bg_color': '#DDEBF7', 'border': 1, 'align': 'center'
    })

    money_format = workbook.add_format({
        'num_format': '[$US$ ]#,##0.00', 'border': 1, 'align': 'center'
    })

    text_format = workbook.add_format({'border': 1, 'align': 'center'})

    for col_num, col_name in enumerate(df.columns):
        worksheet.write(0, col_num, col_name, header_format)
        if 'valor_total_importacao' in col_name.lower():
            worksheet.set_column(col_num, col_num, 25, money_format)
        else:
            worksheet.set_column(col_num, col_num, 25, text_format)

print(f"\n✅ Excel file '{excel_file}' generated successfully!")
