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
#ds1 = pd.read_csv('dataset-part1.csv')
#ds2 = pd.read_csv('dataset-part2.csv')
#ds3 = pd.read_csv('dataset-part3.csv')
ds4 = pd.read_csv('dataset-part4.csv')

#dataset = pd.concat([ds1, ds2, ds3, ds4], axis=1)

#dataset.to_csv('datset.csv')

lis = []
for i in ds4['LABEL']:
    if i != 'Normal flow':
        if i not in lis:
            lis.append(i)

print(lis)


df_agg1 = ds4[ds4['LABEL'] == 'FIN Scan'].head(1500)
df_agg2 = ds4[ds4['LABEL'] == 'UDP Scan'].head(1500)

df_agg3 = pd.concat([df_agg1, df_agg2])

#df_agg3 = df_agg3.head(1500)




df_norm = ds4[ds4['LABEL'] == 'Normal flow']
df_norm = df_norm.head(6000)


df_norm.to_csv('df_norm4.csv')
df_agg3.to_csv('df_agg4.csv')
#print(dataset['LABEL'])


df_n1 = pd.read_csv('df_norm1.csv')
df_n2 = pd.read_csv('df_norm2.csv')
df_n3 = pd.read_csv('df_norm3.csv')
df_n4 = pd.read_csv('df_norm4.csv')

df_a1 = pd.read_csv('df_agg1.csv')
df_a2 = pd.read_csv('df_agg2.csv')
df_a3 = pd.read_csv('df_agg3.csv')
df_a4 = pd.read_csv('df_agg4.csv')

df_final = pd.concat([df_n1, df_n2, df_n3, df_n4, df_a1, df_a2, df_a3, df_a4])

df_final.to_csv('dataframe_spl.csv')

print(df_final['LABEL'].value_counts())