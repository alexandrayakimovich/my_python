x=int(input('Введите код города: '))
y=float(input('Введите длительность переговоров, мин: '))
def call_tel(x, y):
    if x==343:
        return y*15
    elif x==381:
        return y*18
    elif x==473:
        return y*13
    elif x==485:
        return y*11
    else:
        return 'не знаю такой город'
if x==343 or x==381 or x==473 or x==485:
    print('Стоимость переговоров составит', call_tel(x,y), 'руб')
else:
    print(call_tel(x,y))
    
