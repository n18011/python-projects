#!/usr/bin/python3

res = int(input('数値入力:'))

def isleap(res):
    if res % 400 == 0:
        return True
    elif res % 100 == 0:
        return False
    elif res % 4 == 0:
        return True
    else:
        return False


if isleap(res):
    print('{}年はうるう年です。'.format(res))
else:
    print('{}年はうるう年ではない。'.format(res))
