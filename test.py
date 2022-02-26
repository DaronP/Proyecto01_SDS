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


df = pd.read_csv('dataframe_spl.csv')
df = df.drop(['Unnamed: 0'], axis=1)


'''for i in df:
    print(df[df['LABEL'] == 'Normal flow'][i].head(20))
    print(df[df['LABEL'] == 'SYN Scan - aggressive'][i].head(20))
    print(df[df['LABEL'] == 'Denial of Service R-U-Dead-Yet'][i].head(20))
    print(df[df['LABEL'] == 'Denial of Service Slowloris'][i].head(20))
    print('\n\n')'''



for i in df['DST_TO_SRC_SECOND_BYTES']:
    count = 0
    for j in i:
        if j == ',':
            count += 1
    
    if count > 1:
        print(i)


