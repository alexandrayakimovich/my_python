a=input('Выбрать фильм: ')
b=input('Выбрать дату (сегодня, завтра): ')
c=input('Выбрать время: ')
d=input('Выбрать количество билетов: ')
print('Выбрали фильм:', a, 'День:', b, 'Время:', c, 'Количество билетов:', d)
if a!='Пятница' and a!='Чемпионы' and a!='Пернатая банда' or b!='сегодня' and b!='завтра':
    print('Ошибка ввода')
else:
    if a=='Пятница' and int(c)==12 or a=='Чемпионы' and int(c)==10:
        x=250
    elif a=='Пятница' and int(c)==16 or a=='Чемпионы' and int(c)==13 or a=='Чемпионы' and int(c)==16 or a=='Пернатая банда' and int(c)==10:
        x=350
    elif a=='Пятница' and  int(c)==20 or a=='Пернатая банда' and int(c)==14 or a=='Пернатая банда' and int(c)==18:
        x=450
    e=x*int(d)
    if b=='завтра':
        e=e*0.95
    if int(d)>=20:
        e=e*0.8
    print('Результат:', e, 'руб.')

 
    
    
