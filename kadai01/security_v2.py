#!/usr/bin/python3
# 山内先生のgithubのsecurity1のディレクトリを開く

import webbrowser, requests, bs4
import operator as op


def github_url_list(url):
    '''
    リポジトリのURLを返す
    '''
    res = requests.get(url, verify=False)
    soup = bs4.BeautifulSoup(res.text, 'lxml')
    tags = soup.select('table td a.js-navigation-open')

    url_list = [tag.get('href') for tag in tags]
    return url_list


def which_open(url_list):
    '''
    山内先生のgithubを開く
    '''
    while True:
        put = input('何章を表示しますか？(０はホーム): ')
        if op.is_(put, 'q'):
            print('終了')
            break
        try:
            int_put = int(put)
            if op.lt(int_put, len(url_list)):
                webbrowser.open('https://github.com{}'.format(url_list[int_put]))
                print('山内先生のgithubを開きます')
                break
            else:
                print('{}章はありません'.format(put))
                continue
        except (ValueError, TypeError, IndexError):
            print('keyが間違っています')
            continue


if __name__ == '__main__':
    url = 'https://github.com/KimiyukiYamauchi/security1.2018/tree/master/jugyo'
    which_open(github_url_list(url))
