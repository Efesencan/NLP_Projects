# -*- coding: utf-8 -*-
# -*- coding: gb18030 -*-
import re

inputFile = open("input.txt", "r", encoding='utf-8')
with open("name.txt", encoding='utf-8') as name:
    name_content = [line.rstrip() for line in name]

with open("pre_titles.txt", encoding='utf-8') as pre_titles:
    pre_titles = [line.rstrip() for line in pre_titles]

with open("post_titles.txt", encoding='utf-8') as post_titles:
    post_titles = [line.rstrip() for line in post_titles]

with open("day.txt", encoding='utf-8') as date:
    day = [line.rstrip() for line in date]

with open("month.txt", encoding='utf-8') as date:
    month = [line.rstrip() for line in date]

# print(date)
with open("location.txt", encoding='utf-8') as location:
    location = [line.rstrip() for line in location]
# print(location)

for line in inputFile:  # iterate for each line

    # RULE for DATES (yılı, ayı, günü)

    if re.search(r'\d+', line):
        match = re.findall(r'\d{2}-\d{2}-\d{1,}', line)
        if len(match):
            for i in match:
                print("Date:", i.strip)
        match = re.findall(r'\d{2}/\d{2}/\d{1,}', line)
        if len(match):
            for i in match:
                print("Date:", i.strip())
        match = re.findall(r'\d{2}\.\d{2}\.\d{1,}', line)
        if len(match):
            for i in match:
                print("Date:", i.strip())

        if 'yıl' in line or 'sene' in line:
            match = re.findall(r'(\d*)\s*yıl', line)
            if len(match):
                for i in match:
                    print("Date:", i)
            else:
                pass  # 3 basamaklı ve daha az yıllar
            match = re.findall(r'(\d*)\s*sene', line)
            if len(match):
                for i in match:
                    print("Date:", i)
        if "'" in line:
            match = re.findall(r"(\d+)'", line)
            if len(match):
                for i in match:
                    print("Date:", i.strip())
    store_long_match = []
    for month_text in month: # 12 Eylül Salı olan case
        if month_text in line:
            my_month = month_text
            for day_text in day:
                if day_text in line:
                    text_day = day_text
                    long_match = re.findall(f'\d*\s*{my_month}\s*{text_day}', line)
                    if len(long_match):
                        for i in long_match:
                            store_long_match.append(i.strip())
                            print("Date:", i.strip())
    for month_text in month: # 12 Eylül 1935
        if month_text in line:
            my_month = month_text
            match = re.findall(f'\d*\s*{my_month}\s*\d*', line)
            if len(match):
                for i in match:
                    show = 1
                    for j in store_long_match:
                        if i in j:
                            show = 0
                    if(show):
                        print("Date:", i.strip())


    # RULE for NAME
    
    


                


    # location (şehri/ilçesi/beldesi/mahallesi/apartmanı/caddesi/bölge/)
