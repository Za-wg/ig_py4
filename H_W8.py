import random
import string

names = ["Miller", "Attwood", "Backer", "Schwarz", "Pinkman", "Wait", "Black", "Royan", "Zitter"]
domains = ["net", "kh", "ru", "info", "edu", "org", "com", "ua"]


def rand_str():
    name = random.choice(names)
    domen = random.choice(domains)
    str_ra = "".join(random.choice(string.ascii_lowercase) for _ in range(0, random.randint(5, 7)))
    int_ra = random.randint(100, 999)
    return f"{name}.{int_ra}@{str_ra}.{domen}"


print(rand_str())
print('_______________________________________________________')

# # ###########################################2

def rand_string(min_limit: int, max_limit: int):
    rand_str_1 = ''.join(random.choice(string.ascii_lowercase) for _ in range(random.randint(min_limit, max_limit)))
    return rand_str_1

min_limit = 20
max_limit = 121

res = rand_string(min_limit, max_limit)
# ###########################################3

def create_spaces(res):
    index = 0
    rand_str_to_list = list(res)
    condition = True
    while condition:
        step = random.randint(1, 10)
        index += step
        if index < len(res):
            rand_str_to_list[index] = " "
        else:
            condition = False
    rand_str = "".join(rand_str_to_list)
    return rand_str

def modify_str(res):
    rand_str_split = res.split()
    result = []
    for word in rand_str_split:
        word = modify_word(word)
        result.append(word)
    return " ".join(result)

def otdeli_tochka(res):
     rr = res + "."
     return rr

def modify_word(word):
    comma_percentage = 0.2
    if random.random() < comma_percentage:
        word = word.capitalize()
    return word

def zapatya(res):
    s = res.split()
    new_s = []
    for _ in range(len(s)):
       new_s.append(s[_])
       new_s.append([' ', ', '][random.randint(0, 1)])
    hal = ''.join(new_s).rstrip(', ')
    return hal

def add_int(res):
   string_ = ""
   res = res.split()
   for index in range(len(res)):
       vubor = random.randint(1, 2)
       rand_int = random.randint(1, 9)
       if vubor == 2:
           string_ += res[index] + " " + str(rand_int) + ' '
       else:
           string_ += res[index] + " "
   return string_

def znak_perenosa(res):
    index = 0
    rand_to_list = list(res)
    condition = True
    while condition:
        step = random.randint(1, 50)
        index += step
        if index < len(res):
            rand_to_list[index] = "\n"
        else:
            condition = False
    rand = "".join(rand_to_list)
    return rand

res = create_spaces(res)
res = modify_str(res) #capitalaze
res = zapatya(res)
res = add_int(res)
res = znak_perenosa(res)
res = otdeli_tochka(res)

print(res)
