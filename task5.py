#!/usr/bin/python3
moves = input("Input: \n")
x = 0
y = 0
for m in moves:
    if m == 'L':
        x = x - 1
    elif m == 'R':
        x = x + 1
    elif m == 'U':
        y = y + 1
    else:
        y = y - 1
print(x == 0 and y == 0)
