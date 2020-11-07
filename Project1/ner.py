# -*- coding: utf-8 -*-
# -*- coding: gb18030 -*-
import re


inputFile = open("input.txt", "r", encoding='utf-8')
# PERSON RELATED FILES
with open("updated_names.txt", encoding='utf-8') as name:
    name_content = [line.rstrip() for line in name]

with open("pre_titles.txt", encoding='utf-8') as pre_titles:
    pre_titles = [line.rstrip() for line in pre_titles]

with open("post_titles.txt", encoding='utf-8') as post_titles:
    post_titles = [line.rstrip() for line in post_titles]

# DATE RELATED FILES
with open("day.txt", encoding='utf-8') as date:
    day = [line.rstrip() for line in date]

with open("month.txt", encoding='utf-8') as date:
    month = [line.rstrip() for line in date]

with open("location.txt", encoding='utf-8') as location:
    location = [line.rstrip() for line in location]
# print(location)

for line in inputFile:  # iterate for each line

    # RULE for DATES (yılı, ayı, günü) ************************************************************************************

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
    for month_text in month:  # 12 Eylül Salı olan case
        if month_text in line:
            my_month = month_text
            for day_text in day:
                if day_text in line:
                    text_day = day_text
                    long_match = re.findall(
                        f'\d*\s*{my_month}\s*{text_day}', line)
                    if len(long_match):
                        for i in long_match:
                            store_long_match.append(i.strip())
                            line = line.replace(i,'')   # added new line
                            print("Date:", i.strip())
    for month_text in month:  # 12 Eylül 1935
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
                        line = line.replace(i,'')
                        print("Date:", i.strip())
    

    match = re.findall(r'[Y-y]ıl[a-zçğıöşü]*\s(\d+)',line)
    if(len(match)):
        for date in match:
            print("Date:",date)
    match = re.findall(r'[S-s]ene[a-zçğıöşü]*\s(\d+)',line)
    if(len(match)):
        for date in match:
            print("Date:",date)
    # RULE for NAME *******************************************************************************************
    names = []
    for pre_title in pre_titles:
        match = re.findall(
            f'{pre_title}\s*([A-ZÇĞİÖŞÜ]+[a-zçğıöşü]*\s[A-ZÇĞİÖŞÜ]*[a-zçğıöşü]*\.*\s*[A-ZÇĞİÖŞÜ]+[a-zçğıöşü]*)', line)
        if len(match):
            for name in match:
                if name not in names:
                    print("Name:", name)
                    line = line.replace(pre_title + ' ' + name, "") # updated here
                    names.append(name)

    for post_title in post_titles:
        match = re.findall(f'([A-ZÇĞİÖŞÜ]+[a-zçğıöşü]*)\s*{post_title}', line)
        if len(match):
            for name in match:
                print("Name:", name)
                line = line.replace(name + ' ' + post_title, "")

    match = re.findall(r'[A-ZÇĞİÖŞÜ][a-zçğıöşü]*\s*[A-ZÇĞİÖŞÜ]*[a-zçğıöşü]*\s*[A-ZÇĞİÖŞÜ]*[a-zçğıöşü]*', line)
    final_name = ''
    if len(match):
        for name in match:
            splitted_names= name.split()
            if(len(splitted_names) > 1):
                for chance in splitted_names:
                    if chance != chance.capitalize():
                        pass
                    else:
                        if chance in name_content: # soyad listesi bul
                            final_name += chance + ' '
            else:
                if splitted_names[0] in name_content:
                    print("Name:",splitted_names[0])
            
    if(len(final_name)):
        split_final = final_name.split()
        if(len(split_final) >= 1):
            print("Name:",final_name.strip())

                        
                        # organizasyon olma ihtimalini göz ardı ediyorum şu an Örn: Efe Şencan Üniversitesi
          
    # RULE for LOCATION ***************************************************************************************************************


    # location (şehri/ilçesi/beldesi/mahallesi/apartmanı/caddesi/bölge/), 'de 'da ya bakılabilir
    # ülkelere ve kısaltmaları eklenecek ()
    # popular dünya şehirleri eklenecek (yapıldı)
    # .. Kültür ve Sanat Merkezi / Merkezi'nde , kalemim Efe'de kalmış, üst tiredfen önceki kelime isim mi diyr kontrol et veya belki zaten replace edilmiş olur yukarda

    
    
    



    #match = re.findall(r'leri\s',line)
    #match = re.findall(r'ları')
    #match = re.findall(r'imiz\s')
    #match = re.findall(r'ımız\s[A-ZÇĞİÖŞÜ]+[a-zçğıöşü]*\s[A-ZÇĞİÖŞÜ]*[a-zçğıöşü]*')
    # hiçbi rütbeli kısıma girmediyse buradan isim listesi kontrol edilecek, orda da yoksa organizasyon büyük iht. ve lokasyon, ama kelime organizasyonda
    # da yoksa kendisini ve yanındaki harfe de bakarak default isim kabul edilcek.
    # Yabancı İsimler

    
