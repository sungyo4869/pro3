import requests
import bs4
#末尾に\をつけると複数行に分けて記述できる。
url = "https://www.data.jma.go.jp/obd/stats/etrn/view/monthly_s3.php" \
    "?prec_no=91&block_no=47936&year=&month=&day=&view="

#requests.get でWeb ページを取得
res = requests.get(url)
soup = bs4.BeautifulSoup(res.content,'html.parser')
print(soup.select('table')[3].select('tr')[1].select('td')[5])