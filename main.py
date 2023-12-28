#Завдання №1

# try:
#     text = input("Ведіть рядок!")
#     num1 = 0
#     for i in (text):
#         if (i == '1' or i == '2' or i == '3' or i == '4' or i == '5'
#                 or i == '6' or i == '7' or i == '8' or i == '9' or i == '0'):
#             num1 += 1
#     result = len(text)-num1
#     print(f'Знайдено літери в кількості: = {result} шт.')
#     print(f'Знайдено цифри в кількості = {num1} шт.')
# except Exception as error:
#     print(error)

### Тут я не розібрався як виключити зі роботи коду подібні знаки(!!"№;%:?*,) так як код читає ті знаки як Букви!
# Можливо є якийсь except?


#Завдфння №2

# text1=input("Ведіть рядок!")
# text2=input("Ведіть символи для пошуку!")
# num1=0
# for i in (text1):
#     for j in (text2):
#         if [i]==[j]:
#             num1+=1
# print(f"В рядку знайдено: {num1} символи!")

#Завдання №3

# text1=input('Ведіть текст!')
# text2=input('Ведіть слово яке хочете замінити!')
# text3=input('Ведіть слово яким хочете замінити!')
# result=text1.replace(text2,text3)
# print(result)