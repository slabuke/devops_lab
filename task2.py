#!/usr/bin/python3
str_key = input("Enter list of keys \n: ").split(" ")
str_val = input("Enter list of values \n: ").split(" ")
dict_fin = {}
for i in range(len(str_key)):
    if i < len(str_val):
        dict_fin[str_key[i]] = str_val[i]
    else:
        dict_fin[str_key[i]] = None
print(dict_fin)
