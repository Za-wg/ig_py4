# ##################################5
my_str = "aaaaaaaaaaaaaaaaaaaaaannnnnnaaaaaaaaaaaahaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaa"
my_set = set(my_str)
my_list = []
for letter in my_set:
    if my_str.count(letter) == 1:
        my_list.append(letter)
print(my_list)
print('________________________________')
# #################################7
str_1 = "Maze Runner:The Scorch Trials"
str_2 = "Maze Runner:The Death Cure"
my_set_1 = set(str_1)
my_set_2 = set(str_2)
sets = my_set_1.intersection(my_set_2)
new_list = list(sets)
my_list = []
for symbol in new_list:
    if str_1.count(symbol) > 1 or str_2.count(symbol) > 1:
        my_list.append(symbol)

result = [symbol for symbol in new_list if symbol not in my_list]
print(result)
print('________________________________')


# Остальные работы,которые были проверены
# ##################################1
my_list = ["Das", "ist", "str", "Lorem", "ipsum", "Crash", "Viking", "Hund", "Arnold", "ska", "qa", "qwerty"]
new_list = []
for index, items in enumerate(my_list):
    if index % 2 != 0:
        new_list.append(items[::-1])
    else:
        new_list.append(items)
print(new_list)
print('________________________________')
# # ##################################2
my_list = ["Das", "ist", "str", "as", "ipsum", "Crash", "Viking", "among", "Arnold", "april", "qa", "qwerty"]
new_list = [word for word in my_list if word[0] == 'a']
print(new_list)
print('________________________________')
# # ##################################3
my_list = ["Das", "ist", "str", "Lorem", "ipsum", "Crash", "Viking", "Hund", "Arnold", "april", "qa", "qwerty"]
new_list = [new_list for new_list in my_list if "a" in new_list]
print(new_list)
print('________________________________')
# # ##################################4
my_list = ["Das", 6, 12, 32, "str", 98, "Lorem", 4, "Crash", "Viking", "Hund", 8, "april", "qa", "qwerty"]
new_my_list = [word for word in my_list if isinstance(word, str)]
print(new_my_list)
print('________________________________')
# # ##################################6
str_1 = "The Hunger Games: Catching Fire"
str_2 = "The Hunger Games: Mockingjay"
set_1 = set(str_1)
set_2 = set(str_2)
new_my = list(set_1.intersection(set_2))
print(new_my)
print('________________________________')
# # ##################################8
my_dict = {"Last name": 'Kardash',
           "First name": 'Olivia',
           "age": 22,
           "accommodation": {"country": 'USA',
                             "city": 'LA',
                             "adress": "Thi street"
                             },
           "Job": {"availability": 'yes',
                   "position": 'PM'
                   }
           }
print(my_dict["Job"]["position"])
print('________________________________')
# # ################################9
my_dict_1 = {"Components": {"Cakes": {"Flour": '200gr',
                                      "Milk": '500ml',
                                      "Oil": '10ml',
                                      "Egg": 3
                                      },
                            "Cream": {"Sugar": '100gr',
                                      "Oil": '3mg',
                                      "Vanilla": '2gr',
                                      "Sour cream": '300gr'
                                      },
                            "Glaze": {"Cocoa": '100gr',
                                      "Sugar": '60gr',
                                      "Oil": '2mg'
                                      }
                            }
             }
print(my_dict_1["Components"]["Cream"]["Oil"])
