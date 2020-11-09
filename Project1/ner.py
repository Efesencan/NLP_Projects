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

# LOCATION RELATED FILES
with open("world_cities.txt", encoding='utf-8') as world_cities:
    world_cities = [line.rstrip() for line in world_cities]

with open("city.txt", encoding='utf-8') as cities:
    turkish_cities = [line.rstrip() for line in cities]

with open("countries.txt", encoding='utf-8') as country_list:
    countries = [line.rstrip() for line in country_list]

with open("updated_ilçeler.txt", encoding='utf-8') as ilce_list:
    ilceler = [line.rstrip() for line in ilce_list]

with open("post_location.txt", encoding='utf-8') as post_location:
    post_locations = [line.rstrip() for line in post_location]

# ORGANIZATION RELATED FILES
with open("post_organization.txt", encoding='utf-8') as post_organization:
    post_organizations = [line.rstrip() for line in post_organization]

with open("company.txt", encoding='utf-8') as company_list:
    companies = [line.rstrip() for line in company_list]

with open("teams.txt", encoding='utf-8') as team_list:
    teams = [line.rstrip() for line in team_list]

with open("bank.txt", encoding='utf-8') as bank_list:
    banks = [line.rstrip() for line in bank_list]

line_count = 1
for line in inputFile:  # iterate for each line

    # RULE for DATES (yılı, ayı, günü) ************************************************************************************

    if re.search(r'\d+', line):
        match = re.findall(r'\d{2}-\d{2}-\d{1,}', line)
        if len(match):
            for i in match:
                print("Line "+str(line_count) + ": " + "TIME", i.strip())
                line = line.replace(i,'')
        match = re.findall(r'\d{2}/\d{2}/\d{1,}', line)
        if len(match):
            for i in match:
                print("Line "+str(line_count) + ": " + "TIME", i.strip())
                line = line.replace(i,'')
        match = re.findall(r'\d{2}\.\d{2}\.\d{1,}', line)
        if len(match):
            for i in match:
                print("Line "+str(line_count) + ": " + "TIME", i.strip())
                line = line.replace(i,'')
        if 'yıl' in line or 'sene' in line:
            match = re.findall(r'(\d*)\s*yıl', line)
            if len(match):
                for i in match:
                    print("Line "+str(line_count) + ": " + "TIME", i)
                    line = line.replace(i,'')
            else:
                pass  # 3 basamaklı ve daha az yıllar
            match = re.findall(r'(\d*)\s*sene', line)
            if len(match):
                for i in match:
                    print("Line "+str(line_count) + ": " + "TIME", i)
                    line = line.replace(i,'')
        if "'" in line:
            match = re.findall(r"(\d+)'", line)
            if len(match):
                for i in match:
                    print("Line "+str(line_count) + ": " + "TIME", i.strip())
                    line = line.replace(i,'')
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
                            line = line.replace(i, '')   # added new line
                            print("Line "+str(line_count) +
                                  ": " + "TIME", i.strip())
                            line = line.replace(i,'')
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
                        date_list = i.split()
                        if(len(date_list) > 1):
                            line = line.replace(i, '')
                            print("Line "+str(line_count) +
                                  ": " + "TIME", i.strip())
                            line = line.replace(i,'')

    match = re.findall(r'[Y-y]ıl[a-zçğıöşü]*\s(\d+)', line)
    if(len(match)):
        for date in match:
            print("Line "+str(line_count) + ": " + "TIME", date)
            line = line.replace(date,'')
    match = re.findall(r'[S-s]ene[a-zçğıöşü]*\s(\d+)', line)
    if(len(match)):
        for date in match:
            print("Line "+str(line_count) + ": " + "TIME", date)
            line = line.replace(date,'')
    match = re.findall(r'(\d{4})', line)

    if(len(match)):
        for date in match:
            print("Line "+str(line_count) + ": " + "TIME", date)
            line = line.replace(date,'')

    # RULE for LOCATION ***************************************************************************************************************
    line = line.strip()
    for post_location in post_locations:
        match = re.findall(
            f"[A-ZÇĞİÖŞÜ][a-zçğıöşü\']*\s[A-ZÇĞİÖŞÜ]*[a-zçğıöşü\']*\s*[A-ZÇĞİÖŞÜ]*[a-zçğıöşü\']*\s*{post_location}", line)
        for location in match:
            print("Line "+str(line_count) + ": " +
                  "LOCATION", location.strip())
            line = line.replace(location, '')

    # match = re.findall(
        # r'[[A-ZÇĞİÖŞÜ][a-zçğıöşü]*\s*[A-ZÇĞİÖŞÜ]*[a-zçğıöşü]*\s*]*', line)
    match = re.findall(
        r'[A-ZÇĞİÖŞÜ][a-zçğıöşü]*\s*[A-ZÇĞİÖŞÜ]*[a-zçğıöşü]*\s*[A-ZÇĞİÖŞÜ]*[a-zçğıöşü]*\s*[A-ZÇĞİÖŞÜ]*[a-zçğıöşü]*\s*[A-ZÇĞİÖŞÜ]*[a-zçğıöşü]*\s*[A-ZÇĞİÖŞÜ]*[a-zçğıöşü]*', line)
    if len(match):
        for location in match:
            location_list = location.split()
            final = ""
            for chance in location_list:
                if chance[0].isupper():
                    final += ' ' + chance
                    final = final.strip()
                    if (final in world_cities) or (final in countries) or (final in turkish_cities) or (final in ilceler):
                        print("Line "+str(line_count) +
                              ": " + "LOCATION", final.strip())
                        line = line.replace(final, '')
                else:
                    final = ""

    match = re.findall('([A-ZÇĞİÖŞÜ][a-zçğıöşü]*)li', line)
    if(len(match)):
        for i in match:
            if (i in world_cities) or (i in countries) or (i in turkish_cities) or (i in ilceler):
                print("Line "+str(line_count) + ": " + "LOCATION", i.strip())

    match = re.findall('([A-ZÇĞİÖŞÜ][a-zçğıöşü]*)lı', line)
    if(len(match)):
        for i in match:
            if (i in world_cities) or (i in countries) or (i in turkish_cities) or (i in ilceler):
                print("Line "+str(line_count) + ": " + "LOCATION", i.strip())

    # li-li bitişik yazılırmış örneğin Rizeli (yapıldı)
    # location (şehri/ilçesi/beldesi/mahallesi/apartmanı/caddesi/bölge/bulvarı/sokağı/parkı), 'de 'da ya bakılabilir
    # ülkelere ve kısaltmaları eklenecek ()
    # popular dünya şehirleri eklenecek (yapıldı)
    # kıtalarn (eklendi)
    # ...Stadı, Meydanı, ...Merkezi, Caddesi, ...Bölgesi,
    # .. Kültür ve Sanat Merkezi / Merkezi'nde , kalemim Efe'de kalmış, üst tiredfen önceki kelime isim mi diyr kontrol et veya belki zaten replace edilmiş olur yukarda

    # RULE for ORGANIZATION************************************************************************************

    for post_organization in post_organizations:
        match = re.findall(
            f'[A-ZÇĞİÖŞÜ]*[a-zçğıöşü]*\s*[A-ZÇĞİÖŞÜ]*[a-zçğıöşü]*\s*[A-ZÇĞİÖŞÜ]*[a-zçğıöşü]*\s*[A-ZÇĞİÖŞÜ]*[a-zçğıöşü]*\s*[A-ZÇĞİÖŞÜ]+[a-zçğıöşü]*\s{post_organization}', line)
        if(len(match)):
            for i in match:
                final = ""
                organization_list = i.split()
                for chance in organization_list:
                    if chance[0].isupper() or chance == 've':
                        final += chance + ' '
                    if chance == '-':
                        final += chance
                final = final.strip()
                print("Line "+str(line_count) + ": " + "ORGANIZATION", final)
                line = line.replace(final, '')

    # partiler ve kısaltmalar (NATO, UNICEF)
    match = re.findall(r'[A-ZÇĞİÖŞÜ]{2,}', line)
    if (len(match)):
        for organization in match:
            if organization not in name_content and organization not in countries:
                if organization != 'CEO' and organization != 'CTO' and organization != 'CFO':
                    print("Line "+str(line_count) + ": " +
                          "ORGANIZATION", organization)
                    line = line.replace(organization, '')

    for company in companies:
        match = re.findall(f'{company}', line)
        if len(match):
            for i in match:
                print("Line "+str(line_count) +
                      ": " + "ORGANIZATION", i.strip())
                line = line.replace(i, '')

    for team in teams:
        match = re.findall(f'{team}', line)
        if len(match):
            for i in match:
                print("Line "+str(line_count) +
                      ": " + "ORGANIZATION", i.strip())
                line = line.replace(i, '')

    # RULE for NAME *******************************************************************************************
    line = line.strip()
    names = []
    for pre_title in pre_titles:
        match = re.findall(
            f'{pre_title}\s*([A-ZÇĞİÖŞÜ]+[a-zçğıöşü]*\s*[A-ZÇĞİÖŞÜ]*[a-zçğıöşü]*\.*\s*[A-ZÇĞİÖŞÜ]*[a-zçğıöşü]*)', line)  # buraya bi bak
        if len(match):
            for name in match:
                check_list = name.split()
                final = ""
                for chance in check_list:
                    if chance[0].isupper():
                        final += chance + ' '
                final = final.strip()
                if final not in names:
                    if(len(check_list) <= 1):
                        if pre_title == 'Sayın' or pre_title == 'Sevgili':
                            if final not in name_content:
                                pass
                        else:
                            print("Line "+str(line_count) +
                                  ": " + "PERSON", final)
                            line = line.replace(
                                pre_title + ' ' + final, "")  # updated here
                            names.append(final)
                    else:
                        print("Line "+str(line_count) + ": " + "PERSON", final)
                        line = line.replace(
                            pre_title + ' ' + final, "")  # updated here
                        names.append(final)

    for post_title in post_titles:
        match = re.findall(f'([A-ZÇĞİÖŞÜ]+[a-zçğıöşü]*)\s*{post_title}', line)
        if len(match):
            for name in match:
                print("Line "+str(line_count) + ": " + "PERSON", name)
                line = line.replace(name + ' ' + post_title, "")

    match = re.findall(
        r'[A-ZÇĞİÖŞÜ][a-zçğıöşü]*\s*[A-ZÇĞİÖŞÜ]*[a-zçğıöşü]*\s*[A-ZÇĞİÖŞÜ]*[a-zçğıöşü]*', line)
    final_name = ''
    if len(match):
        for name in match:
            splitted_names = name.split()
            if(len(splitted_names) > 1):
                for chance in splitted_names:
                    if (chance[0].isupper() == False):
                        if chance == 'ile' or chance == 've':
                            if(len(final_name)):
                                split_final = final_name.split()
                                if(len(split_final) >= 1):
                                    print("Line "+str(line_count) + ": " +
                                        "PERSON", final_name.strip())
                            final_name = ''
                        else:
                            pass
                    else:
                        if chance in name_content:  # soyad listesi bul
                            final_name += chance + ' '
            else:
                if splitted_names[0] in name_content:
                    print("Line "+str(line_count) + ": " +
                          "PERSON", splitted_names[0])

    if(len(final_name)):
        split_final = final_name.split()
        if(len(split_final) >= 1):
            print("Line "+str(line_count) + ": " +
                  "PERSON", final_name.strip())

            # organizasyon olma ihtimalini göz ardı ediyorum şu an Örn: Efe Şencan Üniversitesi

    #match = re.findall(r'leri\s',line)
    #match = re.findall(r'ları')
    #match = re.findall(r'imiz\s')
    #match = re.findall(r'ımız\s[A-ZÇĞİÖŞÜ]+[a-zçğıöşü]*\s[A-ZÇĞİÖŞÜ]*[a-zçğıöşü]*')
    # hiçbi rütbeli kısıma girmediyse buradan isim listesi kontrol edilecek, orda da yoksa organizasyon büyük iht. ve lokasyon, ama kelime organizasyonda
    # da yoksa kendisini ve yanındaki harfe de bakarak default isim kabul edilcek.
    # Yabancı İsimler

    line_count += 1
