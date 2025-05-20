#FUNCIONALIDADE = ler arquivo de saida em xls de outro script para remover os acentos

import pandas as pd
from unidecode import unidecode

# Caminho do arquivo original
arquivo_entrada = "entrada.xlsx" 
# Ler o Excel ou CSV
df = pd.read_excel(arquivo_entrada)  

# Função para remover acentos de todos os textos
def remover_acentos_df(dataframe):
    for coluna in dataframe.select_dtypes(include=["object"]):
        dataframe[coluna] = dataframe[coluna].astype(str).apply(unidecode)
    return dataframe

# Aplicar função
df_limpo = remover_acentos_df(df)

# Salvar resultado
df_limpo.to_excel("saida_sem_acentos.xlsx", index=False)  