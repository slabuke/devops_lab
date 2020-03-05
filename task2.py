#!/usr/bin/python3
str_key = input().split()
str_val = input().split()
dict_fin = {}
for i in range(len(str_key)):
    if i < len(str_val):
        dict_fin[str_key[i]] = str_val[i]
    else:
        dict_fin[str_key[i]] = None
tmp_string = str(dict_fin)

print(tmp_string.replace("'", ''))
