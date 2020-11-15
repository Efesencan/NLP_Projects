CS 445
Natural Language and Processing
Fall 2020-2021

Project 1: 
Lexicon and Rule-based Named Entity Recognition

Recognizing Date:

There are 2 date related files containing lexicons: day.txt and month.txt. 
Both files are created manually.
Regular Expressions:
1) match = re.findall(r'\d{2}-\d{2}-\d{1,}', line)
	This regex matches the date with the DD-MM-YYYY format. Since there are not any restrictions with the year, the number of digits for the year could be one or greater.
2) match = re.findall(r'\d{2}/\d{2}/\d{1,}', line)
	This regex matches the date with the DD/MM/YYYY format. Since there are not any restrictions with the year, the number of digits for the year could be one or greater.
3) match = re.findall(r'\d{2}\.\d{2}\.\d{1,}', line)
	This regex matches the date with the DD.MM.YYYY format. Since there are not any restrictions with the year, the number of digits for the year could be one or greater.

4) match = re.findall(r'(\d*)\s*yıl', line)
	This regex mathces the years(in digit format) in which the substring ‘yıl’ occurs right afterwards.
	Ex: ‘456 yılında doğmuş.’

5) match = re.findall(r'(\d*)\s*sene', line)
This regex mathces the years(in digit format) in which the substring ‘sene occurs right afterwards.
Ex: ‘1234 senesinde’

6) long_match = re.findall(f'\d*\s*{my_month}\s*{text_day}', line)
This regex mathces the date with the format as follows: (Ex: 12 Eylül Salı)

7) match = re.findall(f'\d*\s*{my_month}\s*\d*', line)
This regex matches the date with the format as follows: (Ex: 12 Eylül 1935). The year after the month is not necessary. For instance ’12 Eylül’ is also valid for this regex.

8) match = re.findall(r'[Y-y]ıl[a-zçğıöşü]*\s(\d+)', line)
This regex matches the substrings with the following format: ex, ‘Yıl 1657’ or ‘Yıllardan 1987’

9) match = re.findall(r'[S-s]ene[a-zçğıöşü]*\s(\d+)', line)
This regex matches the substrings with the following format, ex: ‘Sene 745’ or ‘Senelerden 1987’

10) match = re.findall(r'(\d{4})', line)
This regex matches the substrings that includes 4 digit numbers.

Recognizing Location:

There are 6 location related files in my corpus. These are world_cities.txt, city.txt,   countries.txt, updated_ilçeler.txt, semt_ve_beldeler.txt and post_location.txt. Only post_location.txt is created manually. Others were taken from the Internet. The references of the files are at the end of the file. Since the datasets taken from the Internet was raw, some preprocessing steps were reuired. The codes of the preprocessing steps could be reached from the submitted python files.
The Number of entries each file contains is as follows:
	world_cities.txt: 79160
	city.txt: 88
	countries.txt: 257
	updated_ilçeler.txt: 973
	semt_ve_beldeler.txt: 1767

11) match = re.findall(f"[A-ZÇĞİÖŞÜ]+[a-zçğıöşü\']*\s[A-ZÇĞİÖŞÜ]*[a-zçğıöşü\']*\s*[A-ZÇĞİÖŞÜ]*[a-zçğıöşü\']*\s*{post_location}", line)
This regex matches the substrings in which post_location terms come after the strings. Example mathced substring is as follows: “Kaz Dağları, Ihlara Vadisi, etc.,”

12) match = re.findall( r'[A-ZÇĞİÖŞÜ][a-zçğıöşü]*\s*[A-ZÇĞİÖŞÜ]*[a-zçğıöşü]*\s*[A-ZÇĞİÖŞÜ]*[a-zçğıöşü]*\s*[A-ZÇĞİÖŞÜ]*[a-zçğıöşü]*\s*[A-ZÇĞİÖŞÜ]*[a-zçğıöşü]*\s*[A-ZÇĞİÖŞÜ]*[a-zçğıöşü]*', line)
This regex matches the possible locations which may constituted from one or multiple words. Based on the mathced options, I check whether that location occurs in my corpus. Example match: Amerika Birleşik Devletleri

13) match = re.findall('([A-ZÇĞİÖŞÜ][a-zçğıöşü]*)li', line)
This regex matches the location names in which the string 'li' comes afterwards. Ex: When the input is 'Rizeli', this returns 'Rize' as a location.

14) match = re.findall('([A-ZÇĞİÖŞÜ][a-zçğıöşü]*)lı', line)
This regex matches the location names in which the string 'lı' comes afterwards.

15) match = re.findall('([A-ZÇĞİÖŞÜ][a-zçğıöşü]*\s*[A-ZÇĞİÖŞÜ]*[a-zçğıöşü]*)\skasabası', line)
Since containing all the towns of the world in my corpus is impossible, I wrote this regex in order to capture the following texts as such as 'Ebu Hadi kasabası'.

16) match = re.findall('([A-ZÇĞİÖŞÜ][a-zçğıöşü]*\s*[A-ZÇĞİÖŞÜ]*[a-zçğıöşü]*)\sköyü', line)
Since containing all the villages of the world in my corpus is impossible, I wrote this regex in order to capture the following texts as such as 'xxx(example) köyü'.

17) match = re.findall('([A-ZÇĞİÖŞÜ][a-zçğıöşü]*\s*[A-ZÇĞİÖŞÜ]*[a-zçğıöşü]*)\silçesi', line)
Althogh I have all the Turkish districts in my corpus, I wrote this regex in case there are input texts that contains 'xxx ilçesi' in which 'xxx' is the district name outside from Turkey.

18) match = re.findall('([A-ZÇĞİÖŞÜ][a-zçğıöşü]*\s*[A-ZÇĞİÖŞÜ]*[a-zçğıöşü]*)\smahallesi', line)
This regex matches the substrings which contains 'xxx mahallesi' in it.

Recognizing Organizations:
There are 6 different organization related files in my corpus. These are post_organization.txt, company.txt, teams.txt, bank.txt, university.txt, goverment_organization.txt.
The entities in these files are either taken from the Internet or created manually. Some of the datasets were preprocessed, the preprocessing codes could be reached from the submitted files.The references of the source of the datasets are in the reference part.
The number of entries each file contains is as follows:
	post_organization.txt: 113
	company.txt: 2263
	teams.txt: 415
	university.txt: 190
	goverment_organization.txt: 12

19) match = re.findall(f'[A-ZÇĞİÖŞÜ]+[a-zçğıöşü]*\s*[A-ZÇĞİÖŞÜ]*[a-zçğıöşü]*\s*[A-ZÇĞİÖŞÜ]*[a-zçğıöşü]*\s*[A-ZÇĞİÖŞÜ]*[a-zçğıöşü]*\s*[A-ZÇĞİÖŞÜ]*[a-zçğıöşü]*\s*[A-ZÇĞİÖŞÜ]*[a-zçğıöşü]*\s*[A-ZÇĞİÖŞÜ]*[a-zçğıöşü]*\s{post_organization}', line).
This regex mathces the substrings in which words from post_organization.txt comes afterwards. The example match is as follows: 'Radyo ve Televizyon Üst Kurulu' since 'Kurulu' exists in the post_organization corpus.

20) match = re.findall(r'[A-ZÇĞİÖŞÜ]{2,}', line)
This regex matches the organizations in the form of abbreviations which consists of at least 2 characters. Example matches: 'UNICEF','NATO','CHP'

21) match = re.findall(f'{company}', line)
This regex mathces the companies that exists in my company.txt corpus. Example match: 'Google'

22) match = re.findall(f'{team}', line)
This regex mathces the teams that exists in my teams.txt corpus. Example match: 'Anadolu Efes'

23) match = re.findall(f'{bank}', line)
This regex matches the banks that exists in my bank.txt corpus. Example match: 'Akbank'

24) match = re.findall(f'{university}', line)
This regex matches the universities that exists in my university.txt corpus. Example match: 'Sabancı Üniversitesi'

25) match = re.findall(f'{gov_organization}', line)
This regex matches the goverment related terms that exists in my goverment_organization.txt corpus. The file also contains some terror organizations. Example match: 'Beyaz Saray'

Recognizing Persons:
There are 5 different person related files in my corpus. These are updated_names.txt, male_names.txt, female_names.txt, pre_titles.txt, post_titles.txt. These datasets were mostly taken from the Internet. The source of the datasets are in the reference part.
The number of entries each file contains is as follows:
	updated_names.txt: 12759
	male_names.txt: 47678
	female_names.txt: 25296
	pre_titles.txt: 64
	post_titles.txt: 9

26) match = re.findall(f'{pre_title}\s*([A-ZÇĞİÖŞÜ]+[a-zçğıöşü]*\s*[A-ZÇĞİÖŞÜ]*[a-zçğıöşü]*\.*\s*[A-ZÇĞİÖŞÜ]*[a-zçğıöşü]*)', line)
This regex matches the strings in which pre_titles occurs right before the substrings: Example match: 'Prof. Dr. Yusuf Leblebici' where 'Prof. Dr.' exists in my pre_title.txt corpus.

27) match = re.findall(f'([A-ZÇĞİÖŞÜ]+[a-zçğıöşü]*)\s*{post_title}', line)
This regex matches the strings in which post_title occurs right after the strings. Exampla macth: 'Ali Hoca', where 'Hoca' exists in my post_title.txt corpus.

28) match = re.findall(r'[A-ZÇĞİÖŞÜ][a-zçğıöşü]*\s*[A-ZÇĞİÖŞÜ]*[a-zçğıöşü]*\s*[A-ZÇĞİÖŞÜ]*[a-zçğıöşü]*\s*[A-ZÇĞİÖŞÜ]*[a-zçğıöşü]*', line)
This regex matches the strings which are possible names with at most 4 words.After the match, my script checks whether the matched string exists in my name corpus.

29) match = re.findall(r'[A-ZÇĞİÖŞÜ]+[a-zçğıöşü]*\s[A-ZÇĞİÖŞÜ][a-zçğıöşü]*', line)
This regex mathces the possible foreign names which consists of 2 words. Example match: 'Jason Kidd'

30) match = re.findall(r'[A-ZÇĞİÖŞÜ]\.[A-ZÇĞİÖŞÜ]*\.*[A-ZÇĞİÖŞÜ]*\.*', line)
This regex mathces the possible foreign names which consists of single word. Example match: 'Michael'

REFERENCES:

1) For pre_titles.txt file:
	https://www.buyuknet.com/akademik-unvanlar-siralamasi-t47277.0.html
	https://mfa.gov.ct.tr/wp-content/uploads/2014/02/devlet_protokol_listesi.pdf

2) For names:
	ismailbaskin/turkce_isimler.sql
	https://raw.githubusercontent.com/eoner/turkce_isimler/master/tr_isim_erkek.csv
	https://raw.githubusercontent.com/solvenium/names-dataset/master/dataset/Male_given_names.txt (Male names worldwide)
	https://raw.githubusercontent.com/solvenium/names-dataset/master/dataset/Female_given_names.txt (Female names wordwide)

3) For Locations:
	https://tr.wikipedia.org/wiki/T%C3%BCrkiye%27nin_illeri (Turkish cities)
	https://github.com/FinNLP/cities-list/blob/master/list.txt (World Cities)
	https://tr.wikipedia.org/wiki/T%C3%BCrkiye%27nin_il%C3%A7eleri (For districts in Turkey)
	https://github.com/semihferik/il-ilce-semt-mahalle/blob/master/data/pk_list_07.10.2020.xlsx (For Turkish villages and towns)

4) For Organizations:
	https://gist.github.com/hicay/d2b0035db00e87c207c0 (Turkish Universities)
	https://github.com/mvila/big-companies/blob/master/data.json (Popular companies worldwide)
	https://github.com/smazcw3/European-Soccer-Data/blob/master/team.csv (Some Soccer Teams)
	https://en.wikipedia.org/wiki/List_of_football_clubs_in_Turkey (Turkish Soccer Teams)
	https://www.tbf.org.tr/ligler/bsl-2020-2021/takimlar		(Turkish Basketball Teams)
	https://github.com/ThomasRoca/DataTools-for-Data-science-Society-Datathon-2018 (Forbes top 2000 companies)



