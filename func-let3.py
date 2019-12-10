#!/usr/bin/python3

def calc_5_3(func):
    return func(5, 3)

result = calc_5_3(lambda a, b: a * b)
print(result)

result = calc_5_3(lambda a, b: a + b)
print(result)
