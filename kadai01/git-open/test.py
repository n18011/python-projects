import csv
from web_open import *

csv_list = open_csv('url.csv')
every_dic = {csv_list[i][0]: csv_list[i][1] for i in range(len(csv_list))}
print(every_dic)
new_user = input('新規ユーザー登録: ')
if new_user in every_dic.keys():
    print('存在する')
