##EXTRAÇÃO 

import pandas as pd
import numpy as np


df1_csv = pd.read_csv('spotify_data clean.csv')
df2_csv = pd.read_csv('track_data_final.csv')

#print(df1_csv.info())
#print(df2_csv.info())

print(df1_csv.isna().sum())
print(df2_csv.isna().sum())

##TRANSFORMAÇÃO