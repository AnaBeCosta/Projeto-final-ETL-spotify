##EXTRAÇÃO 
print("******Iniciando o processo de ETL para dados do Spotify...******\n")

import pandas as pd
import numpy as np

print("******Iniciando o processo de ETL para dados do Spotify...******\n")


df1_csv = pd.read_csv('spotify_data_clean.csv')
df2_csv = pd.read_csv('track_data_final.csv')

print("******Finalizando o processo de ETL******\n")

##TRANSFORMAÇÃO

#Tranformação da coluna track_duration_ms de milisegundos para minutos
df2_csv['track_duration_min'] = df2_csv['track_duration_ms'] / 60000
df2_csv['track_duration_min'] = df2_csv['track_duration_min'].round(2)

#print(df2_csv.columns)

#Remoção da coluna track_duration_ms
df2_csv = df2_csv.drop(columns=['track_duration_ms'])

#print(df2_csv.info())

print("******Iniciando o processo de transformação******\n")

print('- Checagem de dados duplicados')
duplicados_df1 = df1_csv.duplicated().sum()
duplicados_df2 = df2_csv.duplicated().sum()

if (duplicados_df1 > 0 or duplicados_df2 > 0) :
    df1_csv = df1_csv.drop_duplicates()
    df2_csv = df2_csv.drop_duplicates()
    print('Linhas duplicadas removidas com sucesso!')


print('- Tratamento de valores nulos')
df1_csv.dropna(subset=['artist_followers'], inplace=True)

colunas1 = ['artist_genres', 'artist_name']
colunas2 = ['track_name', 'artist_genres', 'album_name', 'artist_name']

df1_csv[colunas1] = df1_csv[colunas1].fillna('Não informado')
df2_csv[colunas2] = df2_csv[colunas2].fillna('Não informado')

print('- Tratamento de valores nulos')
