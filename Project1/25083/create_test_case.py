import pandas as pd

f = open('test_case.txt', 'w',encoding='utf-8')
news = pd.read_csv('milliyet_derlem.csv')
count = 1
for new in news['summary']:
    if count == 2850:
        f.write(new)
        break
    count += 1
