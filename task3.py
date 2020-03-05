#!/usr/bin/python3
n = int(input())
fact = 1
for i in range(n):
    fact *= i + 1
print("{1}".format(n, fact))
