# Завдання № 1 v1


# try:
#     num = int(input("Ведіть день тижня!: "))
#     if num==1:
#         print(f'Понеділок: {num} день!')
#     if num==2:
#         print(f'Вівторок: {num} день!')
#     if num==3:
#         print(f'Середа: {num} День!')
#     if num==4:
#         print(f'Четверг: {num} День!')
#     if num==5:
#         print(f'П,ятниця: {num} День!')
#     if num==6:
#         print(f'Субота: {num} День!')
#     if num==7:
#         print(f'Неділя: {num} Дунь!')
#     if num<=0:
#         print(f'Та де ти такий день знайшов?\t{num}')
#     if num>=7:
#         print(f'Дай боже стільки вихідних на тиждень!: {num-5}')
# except ValueError as ValueError:
#     print(f'\tДавай друже ще раз тільки цифрами!!!\n {ValueError}')
# finally:
#     print("Goodbye!")

# v2
# try:
#     num1 = int(input('Enter a number: '))
#     if num1<=0 or num1>=7:
#         print(f'Ведіть цифрами від 1 до 7! \n{num1}???')
#     match num1:
#         case 1:
#             print('Понеділок')
#         case 2:
#             print('Вівторок')
#         case 3:
#             print('Середа')
#         case 4:
#             print('Четверг')
#         case 5:
#             print('П ятниця')
#         case 6:
#             print('Субота')
#         case 7:
#             print('Неділя')
# except ValueError as erorr:
#     print(f'Некоректний тип даних! \n{erorr}???')
# print('\n\nend!')
