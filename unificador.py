#FUNCIONALIDADE: comparar duas planilhas e adicionar as colunas que faltam em uma na outra e retornar um merge principal

import pandas as pd

arquivo1 = 'relatorio1.xlsx'  # Arquivo com dados incompletos
arquivo2 = 'relatorio2.xlsx'  # Arquivo com dados completos
saida_csv = 'relatorio_completo.csv'

coluna_chave = 'Código'

df1 = pd.read_excel(arquivo1)
df2 = pd.read_excel(arquivo2)

# Faz a junção com base no código do produto
df_merged = df1.merge(df2, on=coluna_chave, how='left', suffixes=('', '_ref'))

# Preenche os dados faltantes no df1 com os valores do df2
for coluna in df1.columns:
    if coluna != coluna_chave:
        coluna_ref = f'{coluna}_ref'
        if coluna_ref in df_merged.columns:
            df_merged[coluna] = df_merged[coluna].combine_first(df_merged[coluna_ref])

# Remove colunas extras com sufixo "_ref"
colunas_para_remover = [col for col in df_merged.columns if col.endswith('_ref')]
df_final = df_merged.drop(columns=colunas_para_remover)

# Exporta para CSV com separador ";"
df_final.to_csv(saida_csv, sep=';', index=False, encoding='utf-8-sig')

print(f'Relatório completo gerado com sucesso: {saida_csv}')
