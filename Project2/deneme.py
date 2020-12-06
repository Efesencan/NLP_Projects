a = [[1,2,1],[3,4,5]]

liste = []
for i in a:
    i = [j for j in i if j not in]
    liste.append(i)

print(liste)