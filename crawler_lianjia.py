# -*- coding:utf-8 -*-
import re
import requests
import time
 
homepage = 'http://bj.lianjia.com/xiaoqu/'
areas=['fengtai','shijingshan','changping','daxing','shunyi',    \
		'fangshan','mentougou','pinggu','huairou','miyun','haidian','yanqing']

# areas=['miyun','dongcheng','tongzhou','xicheng','chaoyang',     \
		# 'fengtai','shijingshan','changping','daxing','shunyi',    \
		# 'fangshan','mentougou','pinggu','huairou','miyun','haidian','yanqing']

datas=[]

header_info = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
    'Host':'bj.lianjia.com',
    'Connection':'keep-alive',
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Encoding':'gzip, deflate, sdch',
	'Accept-Language':'en-US,en;q=0.8',
	'Cache-Control':'max-age=0',
    }


def main():
	for area in areas:
		area_data=[]
		totalPage=get_area_info(area)
		time.sleep(10)
		pages =[i for i in range(int(totalPage[0][0])+1)][1:]
		for page in pages:
			xiaoquList=get_xiaoqu_info(homepage+area+'/pg'+str(page)+'/')
			area_data.extend(xiaoquList)
			time.sleep(10)
		write_to_file(area,area_data)

def get_area_info(area):
	r = requests.get(homepage+area, verify=False,headers=header_info)
	totalPage_pattern = re.compile('totalPage\":(\d*),\"curPage\":(\d*)}',re.S)
	totalPage = re.findall(totalPage_pattern,r.text)
	return totalPage

def get_xiaoqu_info(url):
	request=requests.get(url,verify=False,headers=header_info)
	xiaoqu_pattern=re.compile('clear\sxiaoquListItem.*?info.*?title.*?_blank\">(.*?)'+
			'<\/a.*?totalPrice.*?<span>(\d*)<\/span>.*?totalSellCount.*?<span>(\d*)<\/span>',re.S)
	xiaoquList = re.findall(xiaoqu_pattern,request.text)   #获取该页面小区信息
	print(xiaoquList)
	return xiaoquList

def write_to_file(area_name,area_data):
	with open(area_name +'.txt','w', encoding="utf-8") as f:
		for data in area_data:
			f.write('  '.join(data)+'\n')



if __name__ == '__main__':
    main()