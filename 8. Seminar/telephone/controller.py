from database import*
from view import*

def main():
    while True:
        num = input_num()
        match num:
            case 1:
                data = input_data()
                write_data(data)
                print("Успешно записано \n")
            case 2:
                data = input_search()
                search_data(data)
                print("Успешно найдено \n")
            case 3:
                data = input_search()
                search_data_for_change(data)
                num_str = input_for_detect()
                new_array_write_change(num_str, input_data())
                print("Успешно изменено \n")
            case 4:
                data = input_del()
                search_data_for_change(data)
                num_str = input_for_del()
                new_array_write(num_str)
                print("Успешно удалено \n")
            case 5:
                print("Выход")
                return()

main()