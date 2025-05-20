#FUNCIONALIDADE = ler arquivo de saida em csv de outro script para remover os acentos

import pandas as pd
from unidecode import unidecode

arquivo_entrada = "saida1.csv"
arquivo_saida = "saida2.csv"

df = pd.read_csv("saida1.csv", sep=';', encoding='utf-8-sig', engine='python')

def remover_acentos_df(dataframe):
    for coluna in dataframe.select_dtypes(include=["object"]):
        dataframe[coluna] = dataframe[coluna].astype(str).apply(unidecode)
    return dataframe

df_limpo = remover_acentos_df(df)

df_limpo.to_csv(arquivo_saida, index=False, sep=';', encoding='utf-8-sig')