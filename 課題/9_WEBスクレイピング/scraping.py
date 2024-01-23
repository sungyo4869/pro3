import requests
from bs4 import BeautifulSoup
import re

# リクエスト送る
def try_fetch_url(url):
    res = requests.get(url)
    if res.status_code == 200:
        return res.text
    else:
        print(f"Failed to fetch the data. Status code: {response.status_code}")
        return None

# データ取り出す
def scrape_data(html):
    temperature_dict = {}
    year = 1890

    soup = BeautifulSoup(html, 'html.parser')
    # 表を取得
    table = soup.select('table')[3]
    
    while year <= 2024:
        row = table.select('tr')[year-1889]
        if not len(row.select('td')) :
            continue
        temperature_list = []
        for i in range(1, 13):
            cell = row.select('td')[i].text
                        
            cell = clean_temperature_data(cell)
        
            temperature_list.append(cell)
            
        temperature_dict[year] = temperature_list
        year += 1
          
    print(temperature_dict)
    return temperature_dict

def clean_temperature_data(temperature_str):
    if temperature_str.strip() == '\u3000' or temperature_str.strip() == '×':
        print("きてるよ")
        return "None"
    else:
        return re.sub(r'[^\d.-]', '', temperature_str)

    
if __name__ == "__main__":
    url = "https://www.data.jma.go.jp/obd/stats/etrn/view/monthly_s3.php?prec_no=91&block_no=47936&year=&month=&day=&view="
    html_content = try_fetch_url(url)

    if html_content:
        scrape_data(html_content)