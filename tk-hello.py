from tkinter import *

import tkinter.messagebox as mb


def say_hello():
    mb.showinfo('挨拶', 'おはようございます')


def say_goodnight():
    mb.showinfo('挨拶', 'おやすみなさい')


root = Tk()
root.title('挨拶')

desc_label = Label(text='以下のボタンを押してください')
desc_label.pack()

hello_button = Button(text='朝', width=8, height=1, command=say_hello)
hello_button.pack()
goodnight_button = Button(text='寝る前', width=8, height=1, command=say_goodnight)
goodnight_button.pack()


root.mainloop()
