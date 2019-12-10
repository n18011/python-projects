def collatz(number):
    if number % 2 == 1:
        return 3 * number + 1
    else:
        return number / 2

n = int(input('数値を入力'))
while n != 1:
    print(collatz(n))
