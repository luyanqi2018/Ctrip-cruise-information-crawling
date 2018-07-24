import requests
import re
from requests.exceptions import RequestException
import time
import json

def get_one_page(url):

    headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
    response = requests.get(url,headers=headers)
    if response.status_code == 200:
        return response.text
    return None


def main():
    url = 'http://cruise.ctrip.com/'
    html = get_one_page(url)
    for item in parse_one_page(html):
        print(item)


def parse_one_page(html):
    pattern=re.compile('class="name">(.*?)</div>.*?class="ellips">(.*?)</span>(.*?)</div>.*?class="price".*?<dfn>(.*?)</dfn><span>(.*?)</span>(.*?)\n.*?</div>',re.S)
    items=re.findall(pattern,html)
    for item in items:
        yield {
        '名称':item[0],
        '时间':item[1]+item[2],
        '价格':item[3]+item[4]+item[5]
        }

main()