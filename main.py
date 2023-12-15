num1 = int(input("Ведіть перше число від 0 до 10:"))
num2 = int(input("Ведіть друге число від 0 до 10:"))
num3 = int(input("Ведіть трете число від 0 до 10:"))
while "num1 >= 11 and num1 <0 or num2 >= 11 and num2 <0 or num3 >= 11 and num3 <0":
    break
    print("erorr")
if (num1 < num2) and (num1 < num3):
    print (f'\n{num1}: min')
elif (num2 < num1) and (num2 < num3):
    print (f'\n{num2}: min')
elif (num3 < num1) and (num3 < num2):
    print (f'\n{num3}: min')
if (num1 > num2) and(num1 < num3):
    print (f'\n{num1}:Середнє арефметичне')
elif (num1 > num3) and (num1 < num2):
    print (f'\n{num1}:Середнє арефметичне')
elif (num2 > num1) and (num2 < num3):
    print (f'\n{num2}:Середнє арефметичне')
elif (num2 > num3) and (num2 < num1):
    print (f'\n{num2}:Середнє арефметичне')
elif (num3 > num1) and (num3 < num2):
    print (f'\n{num3}:Середнє арефметичне')
elif (num3 > num2) and (num3 < num1):
    print (f'\n{num3}:Середнє арефметичне')
if (num1 > num2) and (num1 > num3):
    print (f'\n{num1}: max')
elif (num2 > num1) and (num2 > num3):
    print (f'\n{num2}: max')
elif (num3 > num2) and (num3 > num1):
    print (f'\n{num3}: max')

print('\n\tend!')

