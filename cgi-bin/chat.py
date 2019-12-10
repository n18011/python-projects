#!/usr/bin/python3

import cgi
import cgitb
import os.path
import html

cgitb.enabele()

FILE_LOG = 'chat-log.txt'

def print_html(body):
    print('Content-Type: text/html; charset=utf-8')
    print('')
    print('''
<html><head><meta charset='utf-8'>
<title>チャット</title></head><body>
<h1>チャット</h1>
<div><form>
名前: <input type='text' name='name' size='8'
本文: <input type='text' name='body' size='20'
<input type='submit' value='発言'>
<input type='hidden' name='mode' value='write'>
</form></div><hr>
{0}
</body></html>
        '''.format(body))


def mode_read(form):
    log = ''
    if os.path.exists(FILE_LOG):
        with open(FILE_LOG, 'r', encoding='utf-8') as f:
            log = f.read()
    print_html(log)


def jump(url):
    print('Status: 301 Moved ')
