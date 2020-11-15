# -*- coding: utf-8 -*-
# -*- coding: gb18030 -*-

with open("raw_universities.txt", encoding='utf-8') as university_list:
    f = open("university.txt", "w+",encoding='utf-8')
    for line in university_list:
        index = line.find('>')
        start_index = index
        while(line[index] != '<'):
            index += 1
      
        line = line[start_index+1:index]
        f.write(line + '\n')
    f.close()