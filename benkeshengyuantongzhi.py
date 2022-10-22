# 抓取本科生院的通知100条
# 数据包含：通知链接，通知标题，发布时间
# 保存到csv中
# 定时每天8点进行爬取

import requests
import re
import csv
import time
from datetime import datetime


def One_Plan():
    # 设置启动周期
    Second_update_time = 24 * 60 * 60    

    # 当前时间  
    now_Time = datetime.now()
  
    # 设置 任务启动时间
    plan_Time = now_Time.replace(hour=8, minute=0, second=0, microsecond=0) 
  
    # 设置差值
    delta = plan_Time - now_Time

    first_plan_Time = delta.total_seconds() % Second_update_time
  
    print("距离下一次执行需要%d秒" % first_plan_Time)
  
    return first_plan_Time
  
while True:
    s1 = One_Plan()
  
    time.sleep(s1)

    # 下面开始执行爬虫
  
    # 创建csv文件并写入标题
    f = open('data3.csv','w',encoding='utf-8',newline='')
    mydic = {
        'ul':'通知链接',
        'title':'通知标题',
        'date':'发布时间'
    }
    csvwriter = csv.writer(f)
    csvwriter.writerow(mydic.values())


    n = 1
    while n != 11:
        # 获取数据
        url = "https://www.bkjx.sdu.edu.cn/sanji_list.jsp"

        param = {
            'totalpage': 154,
            'PAGENUM': n,
            'urltype': 'tree.TreeTempUrl',
            'wbtreeid': '1010'
        }

        head = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 Edg/106.0.1370.47',
            'Cookie': 'JSESSIONID=94AEF718BA5882A2B2F2481F49533939'
        }


        resp = requests.get(url=url,params=param,headers=head)
        contant = resp.text
        

        # 解析数据
        obj = re.compile(r'<div style="float:left"><a href="(?P<ul>.*?)" target=_blank title="(?P<title>.*?)" style=.*?<div style="float:right;">\[(?P<date>.*?)\]',re.S)

        result = obj.finditer(contant)

        # 保存数据
        f = open('data3.csv','a',encoding='utf-8',newline='')

        csvwriter = csv.writer(f)
        
        for it in result:
            dic = it.groupdict()
            csvwriter.writerow(dic.values())

        n += 1


    print('over')
  




