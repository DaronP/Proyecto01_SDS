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


descartar = ['biflow_direction',
'direction',
'firewall_event',
'first_switched',
'flow_active_timeout',
'flow_end_milliseconds',
'flow_end_sec',
'flow_id',
'flow_inactive_timeout',
'flow_start_milliseconds',
'flow_start_sec',
'frame_length',
'last_switched',
'max_ip_pkt_len',
'min_ip_pkt_len',
'ooorder_in_pkts',
'ooorder_out_pkts',
'retransmitted_in_bytes',
'retransmitted_in_pkts',
'retransmitted_out_bytes',
'retransmitted_out_pkts',
'src_tos',
'dst_tos',
'sampling_interval']

for i in range(len(descartar)):
    descartar[i] = descartar[i].upper()

descartar.append('Unnamed: 0')
descartar.append('Unnamed: 0.1')

df = pd.read_csv('dataframe_spl.csv')
#print(df.head())
df = df.drop(descartar, axis=1)

byts = df['DST_TO_SRC_SECOND_BYTES'].to_list()

for i in range(len(byts)):
    if ',' in byts[i]:
        
        if len(byts[i]) == 1:

            byts[i] = byts[i].replace(',', '0')
        
        if len(byts[i]) == 2 or len(byts[i]) == 3:
            byts[i] = byts[i].replace(',', '')
        
        if len(byts[i]) > 3:
            s = ''

            for j in byts[i]:
                if j != ',':
                    s += j
                
                if s != '' and j == ',':
                    byts[i] = s
                    break

        if ',' in byts[i]:
            byts[i] = byts[i].strip(',')
        if len(byts[i]) == 0:
            byts[i] += '0'
            
for i in range(len(byts)):
    byts[i] = int(byts[i])

df['DST_TO_SRC_SECOND_BYTES'] = byts

df.to_csv('df_prep.csv')
#print(df.head())