# crawler_lianjia
抓取链家网上北京所有小区的房价信息，存储到MySQL，再根据输入的小区名称查询小区对应的房价。


###用到的第三方库
- requests:用于抓取链家房价信息
- pymysql:用于操作MySQL
- prettytable:用于对查询的结果进行展示
- colorama:用于给查询结果进行上色


###crawler_lianjia.py
![image](https://github.com/skooby2011/crawler_lianjia/blob/master/crawler_demo.png)

###check_price.py

![image](https://github.com/skooby2011/crawler_lianjia/blob/master/check_price_demo.png)
