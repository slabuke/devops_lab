#!/usr/bin/python3
str_key = str(input("Enter list of keys \n: "))
list_key = str_key.split(" ")
str_val = str(input("Enter list of values \n: "))
list_val = str_val.split(" ")
dict_fin = {}
for i in range(len(list_key)):
    if i < len(list_val):
        dict_fin[list_key[i]] = list_val[i]
    else:
        dict_fin[list_key[i]] = "None"
print(dict_fin) \n
