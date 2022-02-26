from operator import concat
from tkinter import EXCEPTION
from cv2 import correctMatches
from matplotlib import pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sb

descartar = ['biflow_direction',
'direction',
'firewall_event',
'flow_active_timeout',
'flow_end_milliseconds',
'flow_end_sec',
'flow_id',
'flow_inactive_timeout',
'flow_start_milliseconds',
'flow_start_sec',
'frame_length',
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
'sampling_interval',
'IPV4_DST_ADDR',
'IPV4_SRC_ADDR',
'L7_PROTO_NAME']

for i in range(len(descartar)):
    descartar[i] = descartar[i].upper()

descartar.append('Unnamed: 0')

df = pd.read_csv('dataframe_spl.csv')

'''corr_df = df.corr(method='pearson')
print(corr_df)
sb.heatmap(corr_df, annot=True)
plt.show()'''

#print(df.head())
df = df.drop(descartar, axis=1)

df = df[df['PROTOCOL_MAP'] != 'ipv6-icmp']


df.loc[df['PROTOCOL_MAP'] == 'tcp', 'PROTOCOL_MAP'] = 0
df.loc[df['PROTOCOL_MAP'] == 'udp', 'PROTOCOL_MAP'] = 1
df.loc[df['PROTOCOL_MAP'] == 'icmp', 'PROTOCOL_MAP'] = 1
df.loc[df['PROTOCOL_MAP'] == 'gre', 'PROTOCOL_MAP'] = 1

print(df['PROTOCOL_MAP'].unique())


byts = df['DST_TO_SRC_SECOND_BYTES'].to_list()
byts2 = df['SRC_TO_DST_SECOND_BYTES'].to_list()

def prep_bytes(byts):
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
    
    return byts

byts = prep_bytes(byts)
byts2 = prep_bytes(byts2)
            
for i in range(len(byts)):
    byts[i] = int(byts[i])

for i in range(len(byts2)):
    byts2[i] = int(byts2[i])





df['DST_TO_SRC_SECOND_BYTES'] = byts
df['SRC_TO_DST_SECOND_BYTES'] = byts2


corr_df = df.corr(method='pearson')
sb.heatmap(corr_df, annot=True)
plt.show()


df.to_csv('df_prep.csv')
#print(df.head())