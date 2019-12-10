my_pets = ['Zophie', 'Pooka', 'Fat-tail']
print('ペットの名前を入力してください。')
name = input()
if name not in my_pets:
    print("{}という名前のペットは飼っていません。".format(name))
else:
    print('{}は私のペットです。'.format(name))
