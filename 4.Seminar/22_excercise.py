n = int(input('Введите кол-во элементов в первом множестве: '))
m = int(input('Введите кол-во элементов во втором множестве: '))

n_set = set()
m_set = set()


def set_input(my_set, set_len):
    for i in range(1, set_len + 1):
        my_set.add(int(input(f'Введите {i} элемент множества : ')))
    print(my_set)


set_input(n_set, n)
set_input(m_set, m)

print(sorted(set.intersection(n_set, m_set)))
