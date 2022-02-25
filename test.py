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
df = df.drop(['Unnamed: 0', 'Unnamed: 0.1'], axis=1)


c = 0
for i in df:
    if c > 46:
        print(df[df['LABEL'] == 'SYN Scan - aggressive'][i].head(20))
        print(df[df['LABEL'] == 'Denial of Service R-U-Dead-Yet'][i].head(20))
        print(df[df['LABEL'] == 'NULL Scan'][i].head(20))
        print(df[df['LABEL'] == 'UDP Scan'][i].head(20))
        print(df[df['LABEL'] == 'Normal flow'][i].head(20))
        print('\n\n')
        c += 1
    
    else:
        c += 1