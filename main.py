num1 = int(input('Ведіть кількість метрів:'))
if 1<=num1 and num1<=1000:
    select = int(input('1:Милі\n2:Ярди\n3:Дюйми\n'))
    if select==1:
        print(f'result:{num1*0.0006214}')
    if select==2:
        print(f'result:{num1*1.0936133}')
    if select==3:
        print(f'result:{num1*39.3700787}')