#!/usr/bin/env python3

import cgi

print('Content-Type: text/html; charset=utf-8')
print('')

print('<pre>')
form = cgi.FieldStorage()

mode = form.getvalue('mode', default='')
print('mode=', mode)

print('--- all params ---')
for k in form.keys():
    print(k, '=', form.getvalue(k))
