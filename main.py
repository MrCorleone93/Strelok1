try:
    text = input("Ведіть рядок!")
    num1 = 0
    for i in (text):
        if (i == '1' or i == '2' or i == '3' or i == '4' or i == '5'
                or i == '6' or i == '7' or i == '8' or i == '9' or i == '0'):
            num1 += 1
    result = len(text)-num1
    print(f'Знайдено літери в кількості: = {result} шт.')
    print(f'Знайдено цифри в кількості = {num1} шт.')
except BaseException as error:
    print(error)

### Тут я не розібрався як виключити зі роботи коду подібні знаки(!!"№;%:?*,) так як код читає ті знаки як Букви!


