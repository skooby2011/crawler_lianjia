# -*- coding:utf-8 -*-
import pymysql
import pymysql.cursors
import os


path = r"C:\Users\yzhang7\Desktop\workspace\crawler\crawler_lianjia\house_price_04"
database_name = "house_price_04"

#获取所有地区文件
files=[x for x in os.listdir(path) if os.path.splitext(x)[1]=='.txt']
#获取所有地区名称
areas=list(map(lambda x: x.rstrip('.txt'),files))

# 打开数据库连接
db=pymysql.connect("localhost","root","aB123456",database_name,charset='utf8mb4')
# 使用cursor()方法获取操作游标
cursor=db.cursor()

def main():
	#创建所有地区数据表
	create_table()
	#插入小区信息
	insert_info()
	#关闭mysql
	db.close


def insert_info():	
	for file in files:
		with open(path+'\\'+file,'r',encoding="utf8") as f:
			id = 1
			for line in f.readlines():
				
				info=line.split()
				xiaoqu,price,total=info[0],int(info[1]),int(info[2])
				name=file.rstrip('.txt')

				sql= "INSERT INTO %s(id,xiaoqu,price,total) VALUES (%s,\'%s\',%d,%d);"%(name,id,xiaoqu,price,total)
				id = id + 1
				print(sql)
				try:
					# 执行sql语句
					cursor.execute(sql)
					# 提交到数据库执行
					db.commit()
				except:
					# 如果发生错误则回滚
					db.rollback()
					
def create_table():
	for area in areas:
		cursor.execute("DROP TABLE IF EXISTS %s"%area)
		sql = """CREATE TABLE %s (
		         id INT(10) PRIMARY KEY,
		         xiaoqu  CHAR(20),
		         price INT(10),  
		         total INT(10))"""%area

		cursor.execute(sql)

if __name__ == '__main__':
    main()