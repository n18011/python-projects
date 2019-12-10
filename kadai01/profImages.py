import bs4, requests

URL = 'http://results.ittf.link/index.php?option=com_fabrik&view=details&formid=99&Itemid=266&rowid=121404&resetfilters=1'
res = requests.get(URL)
res.raise_for_status()

soup = bs4.BeautifulSoup(res.text, 'lxml')
print(soup)
# elems = soup.select()
