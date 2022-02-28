from operator import concat
from tkinter import EXCEPTION
import pandas as pd
import numpy as np
import sklearn
from sklearn.feature_extraction.text import TfidfVectorizer
import pickle
import unicodedata
import re
import contractions
from gensim.parsing.preprocessing import remove_stopwords
from sklearn.feature_extraction.text import CountVectorizer


print('holisinicial')
ds1 = pd.read_csv('dataset-part1.csv')
ds2 = pd.read_csv('dataset-part2.csv')

print(ds1.LABEL.value_counts(), len(ds1))
print(ds2.LABEL.value_counts(), len(ds2))

print(len(ds1.columns))

df_agg1 = ds1[ds1['LABEL'] == 'SYN Scan - aggressive'].head(800000)
df_agg2 = ds2[ds2['LABEL'] == 'Denial of Service R-U-Dead-Yet'].head(800000)

df_agg3 = ds2[ds2['LABEL'] == 'Denial of Service Slowloris'].head(800000)




df_norm = ds1[ds1['LABEL'] == 'Normal flow'].head(400000)
df_norm2 = ds2[ds2['LABEL'] == 'Normal flow'].head(400000)


df_final = pd.concat([df_norm, df_norm2, df_agg1, df_agg2, df_agg3])

df_final.to_csv('dataframe_spl.csv')

print(df_final['LABEL'].value_counts())