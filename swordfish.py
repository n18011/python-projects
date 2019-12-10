name = ''
while True:
    print("your name")
    name = input()
    if name != "masahiro":
        continue
    print("Hello, masahiro. what pass?")
    password = input()
    if password == "swordfish":
        break
print("Hi!")
