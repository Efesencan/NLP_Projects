# -*- coding: utf-8 -*-
# -*- coding: gb18030 -*-

with open("raw_countries.txt", encoding='utf-8') as long_names:
    f = open("countries.txt", "w+",encoding='utf-8')
    for line in long_names:
        count = 0
        index = 0
        first_check = 1
        second_check = 1
        for letter in line:
            if(letter == "'"):
                count += 1
            if(count == 3 and first_check):
                first_check = 0
                start_index = index
            if(count == 4 and second_check):
                end_index = index
                second_check = 0
                name = line[start_index+1:end_index]
                f.write(name+'\n')
                break
            index += 1
  
    f.close()