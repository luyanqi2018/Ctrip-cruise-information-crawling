from bs4 import BeautifulSoup
import re
import requests
def get_one_page(url):

    headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
    response = requests.get(url,headers=headers)
    if response.status_code == 200:
        return response.text
    return None


#通过正则表达式提取
# def BS(html):
	
#     soup=BeautifulSoup(html,'lxml')
#     results=soup.find_all(attrs={"class":"name"})
#     for result in results:
#     	result=str(result)
#     	zz=re.compile('.*?class="name">(.*?)</div>',re.S)
#     	fin_result=re.search(zz,result)
#     	print(fin_result.group(1))



def BS(html):
	soup=BeautifulSoup(html,'lxml')
	aim_place=soup.find_all(name='div',class_="name")
	for i in range(len(aim_place)):
		aim_place=soup.find_all(name='div',class_="name")[i].string
		date=soup.find_all(name='span',class_="ellips")[i].string
		span=soup.find_all(name='div',class_="price")[i]
		price=span.find_all(name='span')
		for a in price:

		
			print('目的地：'+str(aim_place)+','+'出发日期：'+str(date)+','+'价格'+str(a.string))
		# print(type(aim_place))


def main():
    url = 'http://cruise.ctrip.com/'
    html = get_one_page(url)
    BS(html)



main()