num1 = int(input("Ведіть перше число від 0 до 10:"))
num2 = int(input("Ведіть друге число від 0 до 10:"))
num3 = int(input("Ведіть трете число від 0 до 10:"))
if num1 == num2 == num3:
    print('eror')
elif num1 < num2 < num3:
    print (f'\n{num1}: min')
elif num2 < num1 < num3:
    print (f'\n{num2}: min')
elif num3 < num1 < num2:
    print (f'\n{num3}: min')
elif num1 > num2 < num3:
    print (f'\n{num1}:s')
elif num1 > num3 < num2:
    print (f'\n{num1}:s')
elif num2 > num1 < num3:
    print (f'\n{num2}:s')
elif num2 > num3 < num1:
    print (f'\n{num2}:s')
elif num3 > num1 < num2:
    print (f'\n{num3}:s')
elif num3 > num2 < num1:
    print (f'\n{num3}:s')
elif num1 > num2 > num3:
    print (f'\n{num1}: max')
elif num2 > num1 > num3:
    print (f'\n{num2}: max')
elif num3 > num2 > num1:
    print (f'\n{num3}: max')
