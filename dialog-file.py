#!/usr/bin/python3

import tkinter.filedialog as fd

path = fd.askopenfilename(title='処理対象のファイルを指定してください', filetypes=[('HTML', '.html')])
print(path)
