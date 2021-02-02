# ##################################1
my_int = 102030405000006070809
my_int = str(my_int)
print(my_int.count('0'))
# ##################################2
num = 50760700033000000
new_n = str(num)
print(len(new_n) - len(new_n.rstrip('0')))
# Решила двумя способами,но первый кажется лучше
num = 5076070003300
count = 0
for e in str(num)[::-1]:
    if e == '0':
        count += 1
    else:
        break
print(count)
# ##################################3a
my_list_1 = [1, 2, 3, 4, 5, 6, 7, 8]
my_list_2 = [9, 10, 11, 12, 13, 14, 15, 16]
my_result = []
for symbol in my_list_1[1::2]:
    my_result.append(symbol)
for symbol in my_list_2[::2]:
    my_result.append(symbol)
print(my_result)
# ##################################3b
my_list_1 = [1, 3, 2, 4, 5]
my_list_2 = [10, 20, 15, 25, 22]
my_result = []
for element in my_list_1:
    if not element % 2:
        my_result.append(element)
for element in my_list_2:
    if element % 2:
        my_result.append(element)
print(my_result)
# ##################################4
my_list = [1, 2, 3, 4]
new_list = my_list[1:].copy()
new_list.append(my_list[0])
print(new_list)
# ##################################5
my_list = [1, 9, 5, 2]
my_list.append(my_list.pop(0))
print(my_list)
# ##################################6
my_str = "40 больше чем 30 но меньше чем 100"
words = my_str.split(' ')
product = 0
for word in words:
    try:
        value = int(word)
        product += value
    except:
        pass
print(product)
# #################################7
my_str = 'acdbe'
pip = '_'
if len(my_str) % 2:
    my_str = my_str + pip
my_list = [my_str[i:i+2] for i in range(0, len(my_str), 2)]
print(my_list)
# ################################8
my_str = "My_lore str"
l_limit = "o"
r_limit = "t"
sub_str = (my_str[my_str.find(l_limit)+1: my_str.find(r_limit)])
print(sub_str)
# ####################################9
my_str = "Li worem ipsum"
l_limit = "o"
r_limit = "m"
i1 = my_str.find(l_limit)
i2 = my_str.rfind(r_limit)
sub_str = my_str[i1+1:i2]
print(sub_str)
# ##################################10
my_list = [2, 4, 1, 5, 3, 9, 0, 7]
result = 0
for i in range(1, len(my_list) - 1):
    if my_list[i - 1] < my_list[i] > my_list[i + 1]:
        result += 1
print(result)