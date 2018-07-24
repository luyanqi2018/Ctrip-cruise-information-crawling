#encoding=utf-8
from pyquery import PyQuery as pq
import csv


headers={
	'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
	'X-Requested-With':'XMLHttpRequest'
}

def main():
	with open('皇家加勒比.csv','w',encoding='utf-8',newline='') as csvfile:#加入newline=''可以防止写入csv中时出现空行
		writer=csv.writer(csvfile)
		writer.writerow(['航线','title','出发地','出发时间','卖家','内舱','海景','阳台','套房','评价'])
	for i in range (1,10):
		url='http://cruise.ctrip.com/search'+'/c2p'+str(i)+'.html'
		doc=pq(url=url)
		for product in doc('.route_list').items():
			info={
			'route_catgeory':product('.route_category').text(),
			'route_title':product('.route_title').text(),
			'route_info_label':product('.route_info_label').text(),
			'date':product('.txt_link_strong').text(),
			'supplier_items':product('.supplier_items').text(),
			'内舱':product('.route_list_bottom li:nth-child(1) .price').text(),
			'海景':product('.route_list_bottom li:nth-child(2) .price').text(),
			'阳台':product('.route_list_bottom li:nth-child(3) .price').text(),
			'套房':product('.route_list_bottom li:nth-child(4) .price').text(),
			'score':product('.route_score p').text()

			}
			# print(info)
			with open('皇家加勒比.csv','a',encoding='utf-8',newline='') as csvfile:
				writer=csv.writer(csvfile)
				writer.writerow([info['route_catgeory'],info['route_title'],info['route_info_label'],info['date'],info['supplier_items'],info['内舱'],info['海景'],info['阳台'],info['套房'],info['score']])






if __name__ == '__main__':
	main()

