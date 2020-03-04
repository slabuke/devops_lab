#!/usr/bin/python3
n = int(input("Input:\n "))
fact = 1
for i in range(n):
    fact *= i + 1
print("Output:\n {1}".format(n, fact))
