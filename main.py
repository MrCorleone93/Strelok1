num1 = int(input("Ведіть перше число від 0 до 10:"))
num2 = int(input("Ведіть друге число від 0 до 10:"))
num3 = int(input("Ведіть трете число від 0 до 10:"))
if num1 <= num2 <= num3:
    print (f'{num1}: min')
elif 0 <= num1 > 10:
    print (f'{num1} num1:?')
elif 0 <= num2 > 10:
    print (f'{num2} num2:?')
elif 0 <= num3 > 10:
    print (f'{num3} num3:?')



