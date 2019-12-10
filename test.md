# chapter2 exercise

## 2.11

### 2-1

```
# True, False
```

### 2-2

```
# not, and, or
```

### 2-3

```
# not True -> False
# not False -> True

# True and True -> True
# True and False -> False
# False and True -> False
# False and False -> False

# True or True -> True
# True or False -> True
# False or True -> True
# False or False -> False
```

### 2-4

```
# (5 > 4) and (3 == 5) -> False
# not (5 > 4) -> False
# (5 > 4) or (3 == 5) -> True
# not ((5 > 4) or (3 == 5)) -> False
# (True and True) and (True == False) -> False
# (not False) or (not True) -> True
```

### 2-5

```
# ==, >, <, >=, <=, !=
```

### 2-6

- 等値比較演算子は==,両辺が等しいか調べる。
- 代入演算子は=,右辺の値を左辺の変数に代入する。

### 2-7

- ブール式のこと。フロー制御文で用いる。

### 2-8

```
# spam = 0
# if spam == 10:
#   print('eggs')  #1ブロック
#   if spam > 5:
#       print('bacon')  #2ブロック
#   else:
#       print('ham')  #3ブロック
#   print('spam')
# print('spam')
```

### 2-9

```
spam = int(input())
if spam == 1:
    print("Hello")
elif spam == 2:
    print("Howdy")
else:
    print("Greetings!")
```

### 2-10

-　Ctrl + c

### 2-11

- breakはプログラム文が到達するとループ節をぬける。
- continueはループ節の頭から再評価していく。

### 2-12

- range(10)は１０回繰り返す。
- range(0, 10)は０〜９までの１０つの数字を繰り返す。
- range(0, 10, 1)は関数の開始、終了、ステップ数を表す。

### 2-13

```
for i in range(1, 11):
    print(i)
```
```
n = 0
while n < 10:
    n += 1
    print(n)
```

### 2-14

```
# from spam import bacon
# bacon()
```
