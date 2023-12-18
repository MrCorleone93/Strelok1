try:
    num = int(input("Enter a number: "))
    if 1>=num<=7:
        if num==1:
            print(f'Понеділок:{num}день!')
        if num==2:
            print(f'Вівторок:{num}день!')
        if num==3:
            print(f'Середа:{num}')
        if num==4:
            print(f'Четверг:{num}')
        if num==5:
            print(f'П,ятниця:{num}')
        if num==6:
            print(f'Субота:{num}')
        if num==7:
            print(f'Неділя:{num}')
except TypeError as e:
    print(f"Не коректний тип данних! Ведіть числове значення від 1 до 7:\n\n\t\t\t{num} ???")
