from lxml import etree
import requests

def get_one_page(url):

    headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
    response = requests.get(url,headers=headers)
    if response.status_code == 200:
        return response.text
    return None


def Xpath(text):
    html=etree.HTML(text)
    aim_place=html.xpath('//div[@class="name"]/text()')
    date=html.xpath('//div[@class="date"]//text()')
    price=html.xpath('//div[@class="price"]/dfn/text()')
    price_2=html.xpath('//div[@class="price"]/span/text()')
    # print(result)
    for i in range(len(aim_place)):
        print('目的地：'+aim_place[i]+','+'出发日期：'+date[i]+','+'价格：'+price[i]+price_2[i]+'起')

def main():
    url = 'http://cruise.ctrip.com/'
    html = get_one_page(url)
    Xpath(html)


main()