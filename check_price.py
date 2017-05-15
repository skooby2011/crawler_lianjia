# -*- coding:utf-8 -*-
import pymysql
import pymysql.cursors
from prettytable import PrettyTable
from colorama import init, Fore
import pdb
import sys


#数据库名称
database_name = "house_price_04"
# 打开数据库连接
db = pymysql.connect("localhost","root","aB123456",database_name,charset='utf8mb4')
# 使用cursor()方法获取操作游标
cursor = db.cursor()

def main():
	#用于存储查询到包含关键字的小区信息check
	global data
	data = []

	global check_name 
	
	count = 10
	while count > 1 :
		#输入要查询的小区名称
		check_name = input("请输入小区名称：");
		
		if check_name == 'exit' or check_name == 'quit':
			sys.exit()

		# pdb.set_trace() # 运行到这里会自动暂停

		header = '地区 id 小区名称 价格 在售'.split()
		pt = PrettyTable()
		pt._set_field_names(header)

		#获取所有table
		tables = show_tables()
		for table in tables:
			select_info(table)

		for row in data:
			# row_list=list(row)
			new_row = [
					Fore.GREEN + row[0] + Fore.RESET,
					row[1],
					Fore.GREEN + row[2] + Fore.RESET,
					Fore.RED + str(row[3]) + Fore.RESET,
					row[4],
			]
			pt.add_row(new_row)

		print(pt)
		count = count - 1
		data = []

def show_tables():
	sql = "show tables;"
	try:
		cursor.execute(sql)
		tables=cursor.fetchall()
	except:
		print ("Error: unable to fetch table data")
	return tables

def select_info(table):
	sql = "SELECT * FROM %s;" % table
	try:
	   # 执行SQL语句
	   cursor.execute(sql)
	   # 获取所有记录列表
	   results = cursor.fetchall()
	   for row in results:
	   		name = row[1]
	   		if(check_name in name):
	   			area= table[0]
	   			rowList= list(row)
	   			rowList.insert(0, area)
	   			
	   			data.append(rowList)

	except:
	   print ("Error: unable to 小区 data")


if __name__ == '__main__':
    main()