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

	#画出主要plot曲线
	real_range = price_range[1:]
	fig, ax = plt.subplots()
	ax.plot(real_range, data)

	#设置x，y的limits
	# # plt.xlim(real_range.min()*1.1, real_range.max()*1.1)
	plt.ylim(data.min()*1.1,data.max()*1.1)

	ax.set_title('Beijing House Price In April')
	ax.set_xlabel('Price Range')
	ax.set_ylabel('House Volume')

	#画出最高点数值及连线，Annotate point
	t = 55000
	y = 521
	plt.plot([t,t], [0,y], color ='red',  linewidth=1.5, linestyle="--")
	plt.annotate(r'$521$',
             xy=(t, y),xytext=(+15, +5), textcoords='offset points', 
             fontsize=11,arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))
	plt.scatter([t,],[y,], 15, color ='green')

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