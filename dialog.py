#!/usr/bin/python3

import tkinter.messagebox as mb

ans = mb.askyesno('質問', 'ラーメンは好きですか？')
if ans is True:
    mb.showinfo('同意', '僕も好きです')
else:
    mb.showinfo('本当？', 'まさか、ラーメンが嫌いだなんて！')
