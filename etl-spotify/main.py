##EXTRAÇÃO 
print("******Iniciando o processo de ETL para dados do Spotify...******\n")

import pandas as pd
import numpy as np

df1_csv = pd.read_csv('etl-spotify/spotify_data_clean.csv')
df2_csv = pd.read_csv('etl-spotify/track_data_final.csv')
print("******Finalizando o processo de ETL******\n")



##TRANSFORMAÇÃO
print("******Iniciando o processo de transformação******\n")

#Tranformação da coluna track_duration_ms de milisegundos para minutos
df2_csv['track_duration_min'] = df2_csv['track_duration_ms'] / 60000
df2_csv['track_duration_min'] = df2_csv['track_duration_min'].round(2)

#Remoção da coluna track_duration_ms
df2_csv = df2_csv.drop(columns=['track_duration_ms'])

#Remoção dos duplicados
duplicados_df1 = df1_csv.duplicated().sum()
duplicados_df2 = df2_csv.duplicated().sum()

if (duplicados_df1 > 0 or duplicados_df2 > 0) :
    df1_csv = df1_csv.drop_duplicates()
    df2_csv = df2_csv.drop_duplicates()
    print('Linhas duplicadas removidas com sucesso!')

#Tratamento dos nulos
df1_csv.dropna(subset=['artist_followers'], inplace=True)

colunas1 = ['artist_genres', 'artist_name']
colunas2 = ['track_name', 'artist_genres', 'album_name', 'artist_name']
colunas2SemName = ['artist_genres', 'album_name']

df1_csv[colunas1] = df1_csv[colunas1].fillna('Não informado')
df2_csv[colunas2] = df2_csv[colunas2].fillna('Não informado')

##Convertendo formato de data (MM/DD/AA → DD/MM/AA)'
colunas3 = 'album_release_date'

df1_csv[colunas3] = pd.to_datetime(df1_csv[colunas3], format='%m/%d/%y', errors='coerce')
df2_csv[colunas3] = pd.to_datetime(df2_csv[colunas3], format='%m/%d/%y', errors='coerce')

df1_csv[colunas3] = df1_csv[colunas3].dt.strftime('%d/%m/%y')
df2_csv[colunas3] = df2_csv[colunas3].dt.strftime('%d/%m/%y')

#Todos os textos com letras minúsculas
df1_csv[colunas1] = df1_csv[colunas1].apply(lambda col: col.map(lambda x: x.lower() if isinstance(x, str) else x))
df2_csv[colunas2] = df2_csv[colunas2].apply(lambda col: col.map(lambda x: x.lower() if isinstance(x, str) else x))

# Remover espaços início/fim
df1_csv[colunas1] = df1_csv[colunas1].apply(lambda col: col.map(lambda x: x.strip() if isinstance(x, str) else x))
df2_csv[colunas2] = df2_csv[colunas2].apply(lambda col: col.map(lambda x: x.strip() if isinstance(x, str) else x))

# Remover caracteres especiais (mantém a virgula para gêneros musicais)
regex_limpeza = {r'[^\w\s,]': ''}

df1_csv['artist_genres'] = df1_csv['artist_genres'].replace(regex_limpeza, regex=True)
df2_csv[colunas2SemName] = df2_csv[colunas2SemName].replace(regex_limpeza, regex=True)

df1_csv['artist_genres'] = (
    df1_csv['artist_genres']
        .str.replace(", ", ",", regex=False)  # remove espaço inconsistente
        .str.replace(",", ", ", regex=False)  # adiciona espaço padrão
)

df2_csv['artist_genres'] = (
    df2_csv['artist_genres']
        .str.replace(", ", ",", regex=False)
        .str.replace(",", ", ", regex=False)
)

#Preencher os vazios que ficaram na coluna artist_genres após a limpeza
df2_csv['artist_genres'] = df2_csv['artist_genres'].replace('', 'Não informado')

#Analisar frequência de gêneros musicais
generos_df1 = df1_csv['artist_genres'].str.get_dummies(sep=', ')

frequencia1 = generos_df1.sum()
#print(frequencia1.sort_values(ascending=False))

generos_df2 = df2_csv['artist_genres'].str.get_dummies(sep=', ')

frequencia2 = generos_df2.sum()
#print(frequencia2.sort_values(ascending=False))