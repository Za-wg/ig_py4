################################################1
my_list = [1, 3, 54, 123, 321, 432, 24, 243, 234]
for symbol in my_list:
 if symbol > 100:
   print(symbol)
 else:
   print("")
#################################################2
my_list = [1, 3, 54, 123, 321, 432, 24, 243, 234]
my_results = []
for symbol in my_list:
 if symbol > 100:
   my_results.append(symbol)
 else :
   print("")
print(my_results)
#################################################3
my_list = [int(symbol) for symbol in input().split()]
print(my_list.append(0)) if len(my_list) < 2 else print(my_list[-1] + my_list[-2])
print(my_list)
#################################################4
my_indexes = [0, 1, 2, 3, 4, 5, 6]
my_list = list("bonitas")
for index in my_indexes:
 print(my_list[index])
#################################################5
my_indexes = [0, 1, 2, 3, 4, 5, 6]
my_list_1 = list("bonitas")
my_list_2 = list("potiori")
for index in my_indexes:
 print(my_list_1[index], my_list_2[index])
#################################################6
my_string = '0123456789'
my_list = []
for symb_1 in my_string:
 for symb_2 in my_string:
  symbol = int(symb_1 + symb_2)
  my_list.append(symbol)
print(my_list)