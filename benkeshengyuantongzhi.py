# 抓取本科生院的通知100条
# 数据包含：通知链接，通知标题，发布时间
# 保存到csv中

import requests
import re
import csv

# 创建csv文件并写入标题
f = open('data3.csv','w',encoding='utf-8')
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

    f = open('data3.csv','a',encoding='utf-8')

    csvwriter = csv.writer(f)
    
    for it in result:
        dic = it.groupdict()
        csvwriter.writerow(dic.values())

    n += 1


print('over')
