# pooh_string = pooh_string.split()
# print(pooh_string)
# print(type(pooh_string))

################################################################
# pooh_string = 'пара-ра-рам рам-пам-папам па-ра-па-дам'
# def string_check(str):
#     for i in range(len(str)-1):
#         result = 'Парам пам-пам'
#         if str[i].count('а') != str[i+1].count('а'):
#             result = 'Пам парам'
#             break
#     return result
#
# # print(string_check(pooh_string.split()))
# print(list(map(string_check, pooh_string.split())))

#################################################################
pooh_string = 'пара-ра-рам рам-пам-папам па-ра-па-дам'

res = list(map(lambda x: x.count('а'), pooh_string.split()))

def checking(lst):
    flag = True
    for item in res:
        if item != res[0]:
            flag = False
            return flag
    return flag

print('Парам пам-пам') if checking(res) else print('Пам парам')

###################################################################

