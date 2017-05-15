# -*- coding:utf-8 -*-
import pymysql
import pymysql.cursors
import numpy as np
import matplotlib.pyplot as plt
import pdb

#数据库名称
database_name = "house_price_04"
# 打开数据库连接
db = pymysql.connect("localhost","root","aB123456",database_name,charset='utf8mb4')
# 使用cursor()方法获取操作游标
cursor = db.cursor()

#获取2万到15万的房价区间array
price_range = np.arange(10000, 180000, 5000)
#保存对应区间下房屋总量
price_data = []

def main():
	global tables 
	tables = show_tables()

	x = 0
	while x < len(price_range) - 1:
		num = select_price(price_range[x],price_range[x + 1])
		x = x + 1
		price_data.append(num)

	data = np.array(price_data)

	# pdb.set_trace() # 运行到这里会自动暂停

	fig, ax = plt.subplots()
	ax.plot(price_range[1:], data)


	ax.set_title('Beijing House Price In April')
	ax.set_xlabel('Price Range')
	ax.set_ylabel('House Volume')
	
	plt.show()

def select_price(from_price, end_price):
	num = 0
	for table in tables:
		new_table = table[0]
		sql = "SELECT * FROM %s WHERE price>%d AND price<%d;" % (new_table,from_price,end_price)

		try:
			# 执行SQL语句
			cursor.execute(sql)
			# 获取所有记录列表
			results = cursor.fetchall()
			num = num + len(results)

		except:
			print ("Error: fail to select price data")

	return num

def show_tables():
	sql = "show tables;"
	try:
		cursor.execute(sql)
		tables=cursor.fetchall()
	except:
		print ("Error: unable to fetch table info")
	return tables


if __name__ == '__main__':
    main()