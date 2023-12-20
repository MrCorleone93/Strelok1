try:
    num1 = int(input('Ведіть перше число: '))
    num2 = int(input('Ведіть друге число: '))
    print("Ведіть дію:  \n\n(Додати: + ) або (Відняти: - ) або (Помножити: * ) або (Поділити: / )")
    select = input()
    if select !='+':
        if select != '-':
            if select != '*':
                if select !='/':
                    print(f' Некоректна дія! \n{select}')
    if select == '+':
        print(f'result: = {num1+num2}')
    if select == '-':
        print(f'result: = {num1-num2}')
    if select == '*':
        print(f'result: = {num1*num2}')
    if select == '/':
        print(f'result: = {num1/num2}')
except ZeroDivisionError as Error:
    print('Error, >>>На нуль не ділиться!<<<')
except TypeError as Error:
    print('Error, >>>Некоректний тип даних!<<< ')
except ValueError as Error:
    print('Error, >>>Ведіть цифрами і ніяк інакше!<<< ')
print('end!!!')