# ##################################1
my_list = ["Das", "ist", "str", "Lorem", "ipsum", "Crash", "Viking", "Hund", "Arnold", "ska", "qa", "qwerty"]
new_list = []
for index, items in enumerate(my_list):
    if index % 2 != 0:
        new_list.append(items[::-1])
    else:
        new_list.append(items)
print(new_list)
# ##################################2
my_list = ["Das", "ist", "str", "as", "ipsum", "Crash", "Viking", "among", "Arnold", "april", "qa", "qwerty"]
new_list = [word for word in my_list if word[0] == 'a']
print(new_list)
# ##################################3
my_list = ["Das", "ist", "str", "Lorem", "ipsum", "Crash", "Viking", "Hund", "Arnold", "april", "qa", "qwerty"]
new_list = [new_list for new_list in my_list if "a" in new_list]
print(new_list)
# ##################################4
my_list = ["Das", 6, "str", "Lorem", 4, "Crash", "Viking", "Hund", 8, "april", "qa", "qwerty"]
new_my_list = [word for word in my_list if isinstance(word, str)]
print(new_my_list)
# #################################5
my_str = "Lorem Ipsum is simply dummy text."
my_set = set(my_str)
my_list = []
for i in my_set:
    my_list.append(i)
print(my_list)
# ##################################6
str_1 = "The Hunger Games: Catching Fire"
str_2 = "The Hunger Games: Mockingjay"
print((list(set(str_1 + str_2))))
# #################################7
str_1 = "The Hunger Games: Catching Fire"
str_2 = "The Hunger Games: Mockingjay"
my_list = []
for i in str_1:
    k = str_1.find(i) - str_1.rfind(i)
    if k == 0:
        if i in str_2 and str_2.find(i) - str_2.rfind(i) == 0:
            my_list.append(i)
print(my_list)
# ##################################8
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
# ##################################9
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
