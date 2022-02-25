from operator import concat
from tkinter import EXCEPTION
import pandas as pd
import numpy as np
import pickle
from gensim.parsing.preprocessing import remove_stopwords
from sklearn.feature_extraction.text import CountVectorizer
from sklearn import metrics, model_selection


df = pd.read_csv('df_prep.csv')


target = df['LABEL']

features = df.drop(['LABEL'], axis=1)

final_features = features.columns

print('Final features: ', final_features)

featur