from operator import concat
from tkinter import EXCEPTION
import pandas as pd
import numpy as np
import pickle
from gensim.parsing.preprocessing import remove_stopwords
from sklearn.naive_bayes import MultinomialNB
from sklearn import metrics, model_selection
from sklearn import tree
import time


df = pd.read_csv('df_prep.csv')
print(df['LABEL'])

target = df['LABEL']

print('Target: ', target.unique())

features = df.drop(['LABEL'], axis=1)

final_features = features.columns
final_features.drop('Unnamed: 0')

print('Final features: ', final_features)

feature_matrix_train, feature_matrix_test, target_train, target_test = model_selection.train_test_split(features, target, test_size=0.30, random_state=32)


clf = MultinomialNB()
fit_time = time.time()
clf = clf.fit(feature_matrix_train, target_train)
print('El modelo se tardo en fit: ', time.time() - fit_time)

'''clf_pkl_model = open('model_naive_bayes.pkl', 'wb')
pickle.dump(clf, clf_pkl_model)
clf_pkl_model.close()'''

pred_time = time.time()
target_pred = clf.predict(feature_matrix_test)
print('El modelo se tarde en predecir: ', time.time() - pred_time)

print('Matriz de confusion \n',metrics.confusion_matrix(target_test, target_pred))
print('\nAccuracy score: ',metrics.accuracy_score(target_test, target_pred))
print(metrics.classification_report(target_test, target_pred, target_names=['Normal flow', 'SYN Scan - aggressive', 'Denial of Service R-U-Dead-Yet', 'Denial of Service Slowloris']))