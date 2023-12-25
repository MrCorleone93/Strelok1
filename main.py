try:
    text=input("Ведіть рядок!")
    num1=0
    for i in range(len(text)):
        if text[i]=='1':
            num1+=1
        if text[i]=='2':
            num1+=1
        if text[i]=='3':
            num1+=1
        if text[i]=='4':
            num1+=1
        if text[i]=='5':
            num1+=1
        if text[i]=='6':
            num1+=1
        if text[i]=='7':
            num1+=1
        if text[i]=='8':
            num1+=1
        if text[i]=='9':
            num1+=1
        if text[i]=='0':
            num1+=1
    result=len(text)-num1
    print(f'Букв = {result}')
    print(f'Цифр = {num1}')
except BaseException as error:
    print(error)

### Тут я не розібрався як виключити зі роботи коду подібні знаки(!!"№;%:?*,) так як код читає те як Букви!

