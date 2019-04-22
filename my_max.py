x=float(input('Введите первое число: '))
y=float(input('Введите второе число: '))
def my_max(x,y):
    if x>=y:
        return x
    else:
        return y
print('Максимальное число: ', my_max(x,y))


