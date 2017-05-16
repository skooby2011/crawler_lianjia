# crawler_lianjia
- requests抓取链家网上北京所有小区的房价信息，pymysql存储到MySQL.
- 再根据输入的小区名称从MySQL中查询小区对应的房价等信息。
- prettytable对查询的结果进行展示，colorama给查询结果进行着色
- numpy统计房价区间对应的小区总量
- matplotlib对房价区间以及对应小区总量进行图形化展示


### matplotlib_show.py
![image](https://github.com/skooby2011/crawler_lianjia/blob/master/Price_in_April.png)


### crawler_lianjia.py
![image](https://github.com/skooby2011/crawler_lianjia/blob/master/crawler_demo.png)

### check_price.py

![image](https://github.com/skooby2011/crawler_lianjia/blob/master/check_price_demo.png)
