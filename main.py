
numbers_list = [-1,-4,-6,5,8,6]
negative_numbers_list = []
even_numbers_list = []
positive_numbers_list = []
for i in numbers_list:
    if (i < 0) and (i > -10):
        negative_numbers_list+=[i]
    if (i > 0) and (i < 10):
        positive_numbers_list += [i]
        for j in positive_numbers_list:
            if j % 2 == 0 and j not in even_numbers_list:
                even_numbers_list+=[j]




print(end=' ')








