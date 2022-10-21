# 抓取两个uid的前100个关注，并得到交集
# 得到UID，用户昵称，b站等级，粉丝数
# 将数据保存到.csv文件中

import requests
import re
import csv
import time


# 创建csv文件并写入标题
f = open('data2.csv','w',encoding='utf-8',newline='')
mydic = {
    'follows' : '粉丝数',
    'UID' : 'uid',
    'name' : '用户昵称',
    'level' : 'b站等级'
}
csvwriter = csv.writer(f)
csvwriter.writerow(mydic.values())



# 得到两个用户共同关注的账号的uid
n = 1
idlist1 = []
idlist2 = []

while n <= 5:
    url = 'https://api.bilibili.com/x/relation/followings'

    param_a = {
        'vmid': 6888683,
        'pn': n,
        'ps': 20
    }

    param_b = {
        'vmid': 405556501,
        'pn': n,
        'ps': 20
    }

    head = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 Edg/106.0.1370.47'
    }

    resp_a = requests.get(url=url,params=param_a,headers=head)
    resp_b = requests.get(url=url,params=param_b,headers=head)

    obj = re.compile(r'{"mid":(?P<mid>.*?),')

    id_a = obj.finditer(resp_a.text)
    id_b = obj.finditer(resp_b.text)


    for i in id_a:
        idlist1.append(i.group('mid'))

    for i in id_b:
        idlist2.append(i.group('mid'))

    time.sleep(1)
    n +=1

idlist = list(set(idlist1) & set(idlist2))


# 得到数据
for i in idlist:
    url1 = 'https://api.bilibili.com/x/space/acc/info'
    url2 = 'https://api.bilibili.com/x/relation/stat'

    param1 = {
        'mid' : int(i)
    }

    
    param2 = {
        'vmid': int(i)
    }

    resp1 = requests.get(url=url1,params=param1,headers=head)
    resp2 = requests.get(url=url2,params=param2,headers=head)

    # 解析数据
    obj1 = re.compile(r'{"mid":(?P<UID>.*?),"name":"(?P<name>.*?)",.*?"level":(?P<level>.*?),')
    obj2 = re.compile(r'"follower":(?P<follow>.*?)}')

    result1 = obj1.finditer(resp1.text)
    result2 = obj2.finditer(resp2.text)

    # 保存数据
    f = open('data2.csv','a',encoding='utf-8',newline='')

    csvwriter = csv.writer(f)

    for it in result2:
        f.write(it.group('follow'))
        f.write(',')

    for it in result1:
        dic1 = it.groupdict()
        csvwriter.writerow(dic1.values())

    

    time.sleep(1)

    

print('over')


