# -*- coding: utf-8 -*-
# -*- coding: gb18030 -*-

with open("ilçeler.txt", encoding='utf-8') as long_names:
    f = open("updated_ilçeler.txt", "w+",encoding='utf-8')
    for line in long_names:
        index = line.find('\t')
        if index == -1:
            index = line.find(' ')
        line = line[:index]
        f.write(line + '\n')
    f.close()