try:
    num1 = int(input('Ведіть перше число: '))
    num2 = int(input('Ведіть друге число: '))
    print("Ведіть дію: (Додати: + )\n(Відняти: - )\n(Помножити * )\n(Поділити / )")
    select = input()
    if select != '+,-,*,/':
        print(f' Невірна математична дія ! \n >>>{select}<<< ')
    if select == '+':
        print(f'result= {num1 + num2}')
    elif select == '-':
        print(f'result= {num1 - num2}')
    elif select == '*':
        print(f'result= {num1 * num2}')
    elif select == '/':
        print(f'result= {num1 / num2}')
except ZeroDivisionError as Error:
    print('Error, На нуль не ділиться!')
except ValueError as Error:
    print(' Error, Некоректний тип даних !\n Ведіть цифрами !')
print('end!!!')