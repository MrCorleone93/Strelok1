
#Завдання №1


# numbers_list = [-1,-4,-6,5,8,6,3,7]
# negative_numbers_list = []
# even_numbers_list = []
# positive_numbers_list = []
# odd_numbers_list = []
# product_min_negativ_number_and_max_positive_number = []
# index_3_numbers_list = []
# for i in numbers_list:
#     if (i < 0) and (i > -10):
#         negative_numbers_list += [i]
#     if (i > 0) and (i < 10):
#         positive_numbers_list += [i]
#         for j in positive_numbers_list:
#             if j % 2 == 0 and j not in even_numbers_list:
#                 even_numbers_list += [j]
#             if j % 2 == 1 and j not in odd_numbers_list:
#                 odd_numbers_list += [j]
# for p in numbers_list[::3]:
#     index_3_numbers_list += [p*p]
# for f in numbers_list[1:-1:+1]:
#     product_min_negativ_number_and_max_positive_number += [f*f]
# print(f"Список : {numbers_list}")
# print("Сума негативних чисел : {}".format(sum(negative_numbers_list)))
# print("Сума позитивних чисел : {}".format(sum(positive_numbers_list)))
# print("Сума парних чисел : {}".format(sum(even_numbers_list)))
# print("Сума непарних чисел : {}".format(sum(odd_numbers_list)))
# print("Добуток чисел між мінімальним  та максимальним : {}"
#       .format(sum(product_min_negativ_number_and_max_positive_number)))
# print("Добуток чисел з кратними індексами 3 : {}".format(sum(index_3_numbers_list)))


# Завдання №2


# text_list = [1,2,3,4,5,6,7,8,9,0-1,-2,-3,-4,-5,-6]
# positiv_numbers_list = []
# negativ_numbers_list = []
# odd_numbers_list = []
# even_numbers_list = []
# for number in text_list:
#     if number>=0 and number<10 and number not in positiv_numbers_list:
#         positiv_numbers_list.append(number)
#     if number<=0 and number>=-10:
#         negativ_numbers_list.append(number)
#     if number % 2 == 0:
#         even_numbers_list.append(number)
#     if number % 2 == 1:
#         odd_numbers_list.append(number)
# print("Список парних чисел = {}\nСписок непарних чисел = {}"
#       "\nСписок негативних чисел = {}\nСписок позитивних чисел = {}"
#       .format(even_numbers_list,odd_numbers_list,negativ_numbers_list,positiv_numbers_list))