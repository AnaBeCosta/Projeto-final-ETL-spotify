##EXTRAÇÃO 

import pandas as pd
import numpy as np


df1_csv = pd.read_csv('etl-spotify/spotify_data_clean.csv')
df2_csv = pd.read_csv('etl-spotify/track_data_final.csv')

#print(df1_csv.info())
#print(df2_csv.info())



##TRANSFORMAÇÃO

#Tranformação da coluna track_duration_ms de milisegundos para minutos
df2_csv['track_duration_min'] = df2_csv['track_duration_ms'] / 60000
df2_csv['track_duration_min'] = df2_csv['track_duration_min'].round(2)

#print(df2_csv.columns)

#Remoção da coluna track_duration_ms
df2_csv = df2_csv.drop(columns=['track_duration_ms'])

#print(df2_csv.info())
