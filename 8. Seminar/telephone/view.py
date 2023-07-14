def input_num():
    ask = int(input("Выберите действие: \n 1 - Записать данные нового пользователя \n 2 - Поиск по характеристике \n 3 - Изменить пользователя \n 4 - Удалить пользователя \n 5 - Выход \n"))
    return ask
def input_data():
    a = input("Введите id - ")
    a1 = input("Введите ФИО - ")
    a2 = input("Введите телефоне - ")
    a3 = f"{a} , {a1} , {a2}\n"
    return a3

def input_search():
    data = input("Введите характеристику для поиска - ")
    return data

def input_for_change():
    data = input('Введите характеристику которую хотите изменить ')
    return data

def input_for_del():
    data = int(input('введите номер строки которую хотите удалить '))
    return data

def input_for_detect():
    data = int(input('введите номер строки которую хотите изменить '))
    return data

def input_del():
    data = input('Введите характеристику которую хотите удалить ')
    return data
