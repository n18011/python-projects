import time, requests, bs4, urllib3, certifi, webbrowser, pyautogui


def f(pages, url):
    for i in range(1, pages + 1):
        # pagesが奇数のときは飛ばす
        if i % 2 == 0:
            continue

        # ページ番号を変数pageへ格納
        page = 'START: {}?page={}'.format(url, i)
        print(page)

        # request

    # for文終了表示
    else:
        print('FINISHED!!')


def scraping(url):
    # requests
    http = urllib3.PoolManager(
    cert_reqs='CERT_REQUIRED',
    ca_certs=certifi.where())
    res = http.request('GET', url)

    # htmlをテキスト化
    soup = bs4.BeautifulSoup(res.data, 'html.parser')

    # 画像のURLを見つける
    # image = soup.select('img.page_img')
    image = soup.img

    print(image)


def autoStart(url, jpeg):
    duration = 0.25
    # urlでブラウザを開く
    webbrowser.open(url)
    time.sleep(5)

    # menuバーをクリック
    pyautogui.moveTo(1340, 80, duration=duration)
    pyautogui.click()

    # その他のツール上でホバー
    pyautogui.moveTo(1060, 545, duration=duration)
    time.sleep(1)
    # デベロッパーツールをクリック
    pyautogui.moveTo(790, 690, duration=duration)
    pyautogui.click()
    time.sleep(2)

    # elementsの検索
    pyautogui.hotkey('ctrl', 'f')
    time.sleep(1)
    pyautogui.typewrite('data:', 1)
    time.sleep(2)

    # img elementに移動後new Tabを開く
    openNewTab()
    # 表示されたimgページを保存
    saveImage(jpeg)


def openNewTab():
    duration = 0.25
    # img elementに移動後new Tabを開く
    pyautogui.moveTo(980, 134, duration=duration)
    pyautogui.rightClick()
    pyautogui.moveTo(1030, 170, duration=duration)
    time.sleep(1)
    pyautogui.click()
    time.sleep(5)


def saveImage(jpeg):
    # 表示されたimgページを保存
    pyautogui.hotkey('ctrl', 's')
    pyautogui.hotkey('backspace')
    time.sleep(1)
    pyautogui.typewrite(jpeg, 0.05)
    pyautogui.hotkey('enter')
    time.sleep(1)
    pyautogui.hotkey('ctrl', 'w')


def autoNext(url):
    duration = 0.25
    # urlバーをクリック後url入力
    pyautogui.moveTo(870, 75, duration=duration)
    pyautogui.click()
    pyautogui.typewrite(url, 0.05)
    pyautogui.hotkey('enter')
    time.sleep(5)

    # element検索用
    pyautogui.moveTo(763, 190, duration=duration)
    pyautogui.click()
    time.sleep(1)
    pyautogui.hotkey('backspace')
    time.sleep(1)
    pyautogui.typewrite(':', 1)
    time.sleep(1)


def main(url, title, first, pages):
    m = len(str(pages))
    s = '{}_p{:0' + str(m) + '}.jpeg'

    for i in range(first, pages + 1):
        page = '{}?page={}'.format(url, i)
        jpeg = s.format(title, i)
        if i == 1:
            autoStart(page, jpeg)
            continue

        autoNext(page)
        openNewTab()
        saveImage(jpeg)


if __name__ == '__main__':
    # f(23, 'https://www.example.com/1234567890')
    # url = 'https://impress.tameshiyo.me/9784295002560'
    # url = 'https://impress.tameshiyo.me/9784295005370'
    # url = 'https://impress.tameshiyo.me/9784295003389'
    # url = 'https://impress.tameshiyo.me/9784844338269'
    # url = 'https://impress.tameshiyo.me/9784295000890'
    url = 'https://impress.tameshiyo.me/9784295003190'
    # url = 'https://impress.tameshiyo.me/9784844381510'
    # url = 'https://impress.tameshiyo.me/9784295006070'
    # scraping(url)
    # autoStart(url, 'test3.jpeg')
    main(url, 'lead_business', first=1, pages=304)
