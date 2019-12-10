#!/usr/bin/python3

from tkinter import *


def count_text(event):
    s = main_text.get(1.0, END)
    info_label.config(text='{0}文字'.format(len(s)))


root = Tk()
root.title('テキストカウンタ')

main_text = Text(root)
main_text.bind('<key>', count_text)
main_text.pack()

info_label = Label(root)
info_label.pack()

root.mainloop()
