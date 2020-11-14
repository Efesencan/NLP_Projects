import pandas as pd
df = pd.read_csv('Forbes-Global-2000-2018.csv')
with open("company.txt", encoding='utf-8') as company_list:
    companies = [line.rstrip() for line in company_list]

f = open("company.txt", "a",encoding='utf-8')
for company in df['_ - name']:
    if company not in companies:
        f.write(company + '\n')
f.close()




