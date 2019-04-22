x=float(input('Введите число: '))
print('Число четное?')
def get_par(x):
    y=x%2
    if y != 0:
        return False
    else:
        return True
print(get_par(x))
        


