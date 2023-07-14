def write_data(data):
    with open("telephone.txt", "a", encoding="UTF-8") as file:
        file.write(data)


def search_data(name):
    with open("telephone.txt", "r", encoding="UTF-8") as file:
        a = file.readlines()
        for line in a:
            if name in line:
                print(line.strip())


def search_data_for_change(data):
    with open("telephone.txt", "r", encoding="UTF-8") as file:
        a = file.readlines()
        for i in range(len(a)):
            if data in a[i]:
                print(i, a[i].strip())

def new_array_write(n):
    with open("telephone.txt", "r", encoding="UTF-8") as file:
        a = file.readlines()
        new_array = []
        for i in range(len(a)):
            if i !=n:
                new_array.append(a[i])
    with open("telephone.txt", "w", encoding="UTF-8") as file:
        for line in new_array:
            file.write(line)

def new_array_write_change(n,func):
    with open("telephone.txt", "r", encoding="UTF-8") as file:
        a = file.readlines()
        new_array = []
        for i in range(len(a)):
            if i ==n:
                new_array.append(func)
            else:
                new_array.append(a[i])
    with open("telephone.txt", "w", encoding="UTF-8") as file:
        for line in new_array:
            file.write(line)