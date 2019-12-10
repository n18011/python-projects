#数あてゲーム
import random
secret_number = random.randint(1, 20)
print("1から20までの数を当ててください。")

#６回聞く
for guesses_taken in range(1, 7):
    print('数を入力してください。')
    guess = int(input())

    if guess < secret_number:
        print('小さいです。')
    elif guess > secret_number:
        print('大きいです。')
    else:
        break# 当たり！

if guess == secret_number:
    print('当たり！{}回で当たりました！'.format(str(guesses_taken)))
else:
    print('残念。正解は{}でした。'.format(str(secret_number)))
