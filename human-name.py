#!/usr/bin/python3


class HumanName:
    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name


taro = HumanName()
taro.setName('Taro')
print(taro.getName())

jiro = HumanName()
jiro.setName('Jiro')
print(jiro.getName())
print(taro.name)
print(jiro.name)
