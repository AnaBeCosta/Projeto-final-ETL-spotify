##EXTRAÇÃO 
print("******Iniciando o processo de ETL para dados do Spotify...******\n")

import pandas as pd
import numpy as np
import sqlite3 as sql

df1_csv = pd.read_csv('spotify_data_clean.csv')
print("******Finalizando o processo de ETL******\n")



##TRANSFORMAÇÃO
print("******Iniciando o processo de transformação******\n")

#Remoção dos duplicados
duplicados_df1 = df1_csv.duplicated().sum()

if (duplicados_df1 > 0) :
    df1_csv = df1_csv.drop_duplicates()
    print('Linhas duplicadas removidas com sucesso!')

#Tratamento dos nulos
df1_csv.dropna(subset=['artist_followers'], inplace=True)

colunas1 = ['artist_genres', 'artist_name']
colunas2 = ['track_name', 'artist_genres', 'album_name', 'artist_name']
colunas2SemName = ['artist_genres', 'album_name']

df1_csv[colunas1] = df1_csv[colunas1].fillna('Não informado')

# Converter datas automaticamente
colunas3 = 'album_release_date'

df1_csv[colunas3] = pd.to_datetime(df1_csv[colunas3], errors='coerce')

# Formatar para DD/MM/YYYY
df1_csv[colunas3] = df1_csv[colunas3].dt.strftime('%d/%m/%Y')

#Todos os textos com letras minúsculas
df1_csv[colunas1] = df1_csv[colunas1].apply(lambda col: col.map(lambda x: x.lower() if isinstance(x, str) else x))

# Remover espaços início/fim
df1_csv[colunas1] = df1_csv[colunas1].apply(lambda col: col.map(lambda x: x.strip() if isinstance(x, str) else x))

# Remover caracteres especiais (mantém a virgula para gêneros musicais)
regex_limpeza = {r'[^\w\s,]': ''}

df1_csv['artist_genres'] = df1_csv['artist_genres'].replace(regex_limpeza, regex=True)

df1_csv['artist_genres'] = (
    df1_csv['artist_genres']
        .str.replace(", ", ",", regex=False)  # remove espaço inconsistente
        .str.replace(",", ", ", regex=False)  # adiciona espaço padrão
)

#Analisar frequência de gêneros musicais
generos_df1 = df1_csv['artist_genres'].str.get_dummies(sep=', ')

frequencia1 = generos_df1.sum()
#print(frequencia1.sort_values(ascending=False))



#CARGA
# Criar um banco SQLite (arquivos spotify_data_clean e track_data_final.csv).
conexao = sql.connect("spotify.db")
cursor = conexao.cursor()

# Criando tabelas
cursor.execute("""
CREATE TABLE spotify_data_clean (
  track_id TEXT PRIMARY KEY,
  track_name TEXT,
  track_number INTEGER,
  track_popularity INTEGER,
  explicit INTEGER,
  artist_name TEXT,
  artist_popularity INTEGER,
  artist_followers INTEGER,
  artist_genres TEXT,
  album_id TEXT,
  album_name TEXT,
  album_release_date TEXT,
  album_total_tracks INTEGER,
  album_type TEXT,
  track_duration_min REAL
  );
""")

# Salvar os dados tratados.
df1_csv.to_sql("spotify_data_clean", conexao, if_exists="replace", index=False)
print("Tabela 'spotify_data_clean' carregada.\n")

conexao.close()
print("Banco 'spotify.db' criado e carregado com sucesso!\n")