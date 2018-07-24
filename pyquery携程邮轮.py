#encoding=utf-8
from pyquery import PyQuery as pq
import csv



def main():
	doc=pq(url='http://cruise.ctrip.com/')
	aim_place=doc('.m_item_box .name').text().split(' ')
	# print(aim_place)
	date=doc('.date').text().split(' ')
	# print(date)
	price=doc('.price').text().split(' ')
	# print(price)
	with open('携程.csv','w',encoding='utf-8',newline='') as csvfile:#加入newline=''可以防止写入csv中时出现空行
		writer=csv.writer(csvfile)
		writer.writerow(['目的地','出发日期','出发地','价格'])
		for i in range(len(aim_place)):
			print('目的地：'+aim_place[i]+'，出发日期：'+date[2*i]+'，出发地：'+date[2*i+1]+'，价格：'+price[i])
			writer=csv.writer(csvfile)
			# writer.writerow(['目的地'，'出发日期','价格'])
			writer.writerow([aim_place[i],date[2*i],date[2*i+1],price[i]])







main()