#!/usr/bin/python3

import pyperclip as clip
text = clip.paste()


lines = text.split('\n')
clip.copy(join((["* " + i for i in lines])))
