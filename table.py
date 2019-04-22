value = input("Введите атомный номер: ")
if value:
    at_num = int(value)
    if at_num == 3:
        print("Это Li")
    elif at_num == 25:
        print("Это Mn")
    elif at_num == 80:
        print("Это Hg")
    elif at_num == 17:
        print("Это Cl")    
    else:
        print("Что это?!")
else:
    print("Введите атомный номер!")
