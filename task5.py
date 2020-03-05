#!/usr/bin/python3
moves = input()
x = 0
y = 0
for m in moves:
    if m == 'L':
        x -= 1
    elif m == 'R':
        x += 1
    elif m == 'U':
        y += 1
    else:
        y -= 1
print(x == 0 and y == 0)
