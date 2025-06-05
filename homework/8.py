k = 0
for x in ['Н', "В", "Е", "С", "А"]:
    for y in ['Н', "В", "Е", "С", "А"]:
        for z in ['Н', "В", "Е", "С", "А"]:
            for w in ['Н', "В", "Е", "С", "А"]:
                for u in ['Н', "В", "Е", "С", "А"]:
                    g = x+y+z+w+u
                    if (g[0] == 'Н' and g.count('В') == 2 and g.count('Е') <= 1 and g.count('С') <= 1 and g.count('А') <= 1 and g.count('Н') <= 1):
                        k += 1
print(k)