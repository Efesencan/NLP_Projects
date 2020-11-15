# -*- coding: utf-8 -*-
# -*- coding: gb18030 -*-
import pandas as pd

df = pd.read_excel('pk_list_07.10.2020.xlsx', encoding='utf-8')
f = open('semt_ve_beldeler.txt', 'w+', encoding='utf-8')
t = open('mahalleler.txt', 'w+', encoding='utf-8')

semt_beldeler = df['semt_bucak_belde'].unique()
mahalleler = df['Mahalle'].unique()

for i in semt_beldeler:
    i = i.capitalize()
    i = i.replace('\t','')
    i = i.replace(' ','')
    f.write(i+'\n')

for j in mahalleler:
    j = j.capitalize()
    t.write(j+'\n')

