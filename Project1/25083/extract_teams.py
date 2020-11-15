# -*- coding: utf-8 -*-
# -*- coding: gb18030 -*-
import pandas as pd

team_df = pd.read_csv('team.csv')
teams = team_df['team_long_name']

f = open("teams.txt",'w+',encoding='utf-8')
for team in teams:
    f.write(team + '\n')
f.close()