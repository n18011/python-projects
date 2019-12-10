
import requests, bs4, os, datetime, sys



def editFile(x):
    today = datetime.date.today()
    filename = str(today) + 'wish_list'
    os.makedirs(filename, exist_ok=True)
    wish_file = open('{}/wishList.text'.format(filename), 'a')
    wish_file.write(x)
    wish_file.close()



def makeWishList(ans):
    if ans == 'yes':
        rinfo(getURL())
    else:
        info(getURL())



def getURL():
    url = 'https://www.amazon.co.jp/gp/bestsellers/books/2501045051/ref=zg_bs_2501045051_pg_1?ie=UTF8&pg=1'
    html = requests.get(url)
    soup = bs4.BeautifulSoup(html.text, 'lxml')

    url_list = []

    p = 1
    for page in soup.find_all('li', class_='zg_page'):
        if p > 5:
            break
        else:
            pages = page.find('a').get('href')
            url_list.append(pages)
        p += 1
    return url_list



def info(allurl):

    p = 1
    for pages in allurl:
        url = pages
        html = requests.get(url)
        soup = bs4.BeautifulSoup(html.text, 'lxml')

        if p >= 2:
            nextURL = input('次のランキングを表示しますか？(yes or no): ')
            if nextURL == 'no':
                break

        for elem in soup.find_all('div', class_='zg_itemRow'):
            rank = elem.find('span', class_='zg_rankNumber').string.strip()
            name = elem.find_all('div', class_='p13n-sc-truncate')[0].string.strip()
            price = elem.find('span', class_='p13n-sc-price').string.strip()

            print('{} {} {}'.format(rank, price, name))
            p += 1



def rinfo(allurl):

    p = 1
    for pages in allurl:
        url = pages
        html = requests.get(url)
        soup = bs4.BeautifulSoup(html.text, 'lxml')

        if p >= 2:
            nextURL = input('次のランキングを表示しますか？(yes or no): ')
            if nextURL == 'no':
                break

        for elem in soup.find_all('div', class_='zg_itemRow'):
            rank = elem.find('span', class_='zg_rankNumber').string.strip()
            name = elem.find_all('div', class_='p13n-sc-truncate')[0].string.strip()
            price = elem.find('span', class_='p13n-sc-price').string.strip()

            prin = '{} {} {}'.format(rank, price,name)
            print(prin)
            p += 1
            check = input('この商品をリストに追加しますか？(yes or no) :')
            if check == 'yes':
                editFile(prin+ '\n')
            elif check == 'no':
                continue
            else:
                print('終了します')
                sys.exit()






if __name__ == '__main__':
    wish_list = input('欲しい物リストを作成しますか？(yes or no): ')
    makeWishList(wish_list)
