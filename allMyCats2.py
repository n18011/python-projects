cat_name = []
while True:
    print('猫{}の名前を入力してください。（終了するにはEnterキーだけ押してください）'.format(str(len(cat_name) + 1)))
    name = input()
    if name == "":
        break
    cat_name = cat_name + [name]
print("猫の名前は次の通り:")
for name in cat_name:
    print(" " + name)
