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

# Завдання №2
#
# try:
#     num1 = int(input("Enter a number: "))
#     num2 = int(input("Enter another number: "))
#     if num1 == num2:
#         print(f"{num1} Числа рівні між собою! {num2}")
#     while num1 <= num2:
#         print(f'{num1}')
#         num1 += 1
#     print('\n \\\\end!!!\\\\')
# except ValueError as erorr:
#     print("Некоректний тип даних! Ведіть будьласка цифрами! ")
#
#
# Завдання №3
#
# try:
#     num1 = int(input('Ведіть перше число: '))
#     num2 = int(input('Ведіть друге число: '))
#     print("Ведіть дію:  \n\n(Додати: + ) або (Відняти: - ) або (Помножити: * ) або (Поділити: / )")
#     select = input()
#     if select !='+':
#         if select != '-':
#             if select != '*':
#                 if select !='/':
#                     print(f' Некоректна дія! \n{select}')
#     if select == '+':
#         print(f'result: = {num1+num2}')
#     if select == '-':
#         print(f'result: = {num1-num2}')
#     if select == '*':
#         print(f'result: = {num1*num2}')
#     if select == '/':
#         print(f'result: = {num1/num2}')
# except ZeroDivisionError as Error:
#     print('Error, >>>На нуль не ділиться!<<<')
# except TypeError as Error:
#     print('Error, >>>Некоректний тип даних!<<< ')
# except ValueError as Error:
#     print('Error, >>>Ведіть цифрами і ніяк інакше!<<< ')
# print('end!!!')