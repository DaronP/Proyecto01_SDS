from operator import concat
from tkinter import EXCEPTION
import pandas as pd
import numpy as np
import pickle
from gensim.parsing.preprocessing import remove_stopwords
from sklearn.naive_bayes import MultinomialNB
from sklearn import metrics, model_selection


df = pd.read_csv('df_prep.csv')
print(df['LABEL'])

target = df['LABEL']

features = df.drop(['LABEL'], axis=1)

final_features = features.columns

print('Final features: ', final_features)

feature_matrix_train, feature_matrix_test, target_train, target_test = model_selection.train_test_split(features, target, test_size=0.30, random_state=32)


clf = MultinomialNB()
clf = clf.fit(feature_matrix_train, target_train)

target_pred = clf.predict(feature_matrix_test)


print(metrics.accuracy_score(target_test, target_pred))
print('Matriz de confusion /n',metrics.confusion_matrix(target_test, target_pred))
print(metrics.classification_report(target_test, target_pred, target_names=['spam', 'legitimate']))