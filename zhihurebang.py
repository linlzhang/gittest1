# 抓取知乎热榜100条
# 数据至少包含：热点分类，标题，链接，热力值
# 数据保存到excel中

import requests
import json
import re
import csv


# 创建csv文件并写入标题
f = open('data1.csv','w',encoding='utf-8')
mydic = {
    'title':'标题',
    'class':'分类',
    'number':'热力值',
    'ul':'链接'
}
csvwriter = csv.writer(f)
csvwriter.writerow(mydic.values())


n = 0
while n<100:
    # 获取数据
    url = "https://www.zhihu.com/api/v4/creators/rank/hot"

    param = {
        'domain': '0',
        'limit': 20,
        'offset': n,
       'period': 'hour' 
    }

    head = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',
        'cookie': '_zap=9db3abb0-004a-4187-b9ff-1bcefcf21db7; d_c0=AEBXYaWzthWPTjapisXGQUD35c8fm-o7xb4=|1665818159; __snaker__id=Se6VVFvQPU1YKpRj; _9755xjdesxxd_=32; YD00517437729195%3AWM_NI=8GhBr2h36AMiuqYK5mI2WZgELJl0J0%2BwjHiWfMrCDBa8oEMs%2BW4FecxpogmCMH83AZRpiRjxQPrKGbUY%2Bd%2FyNF158KWt7DT7SZlBtVt72yS%2FL3ZqYR846S7N4qQsxXlLVnc%3D; YD00517437729195%3AWM_NIKE=9ca17ae2e6ffcda170e2e6eed6fc3a93a7a3d7ec6f83b88bb3c55e868e8aacc159f5bf8389c54386aa9caaed2af0fea7c3b92afc99a8a3f13aacedfaa2d063b7af97acb8678bee99bbe64f9096a4d1c93ce9a9a6a9ec5da693bea4c74aa3e8a1a6d079e989fca7e869bcb0a188f0498f98f8d4c45292b0a7b3e9749390beacc66a9787e585ae738e9affd6bb4195acf9a5d73d9186a4a3f75eb8e9fe9ad22590ed9692dc5afcecfab4b646f8af9f94fb54b0949a8fe237e2a3; YD00517437729195%3AWM_TID=kLcL5TznurJFEBRVUAbVD6OYhAYVqDIm; _xsrf=d464aef4-c037-4561-aa46-808592df957b; SESSIONID=yoNmQQobJ49WUjaRPwL5sHf8qi0Hs4zDSTeLanuGI2W; captcha_session_v2=2|1:0|10:1665884978|18:captcha_session_v2|88:TlJoVHRuVW5ISXBRQkgrdmpmNUhxRHpmMXV2RUsrMEliTHNxb0pVWERBRHRPZGpkUElURktTd3BwOTBOLzF1eg==|016b7ccd329d99179b893f39f73961a63c7471100289b349a38c8f56ae24543c; JOID=UVsXCkr3uh0kWSwNDP2ISmj8lbkYjtRYQQp9Y2W_jiV4BERsX8XTVU1bLQcPelsCvC_DpyVSSn6W08ALW5nfluo=; osd=U1kWAkj1uBwsWy4PDfWKSGr9nbsajNVQQwh_Ym29jCd5DEZuXcTbV09ZLA8NeFkDtC3BpSRaSHyU0sgJWZvenug=; Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49=1665818168,1665884983; gdxidpyhxdE=tRdcHngpXtH5a7k0zkIV%2BAr7cNK%5CWo9ixy%5CZPS09Qs9LEODD4zzM6AYYKascoLnpLqYWUAHzH75zB52q%2BcutwTfcH2J5rVrkc%2B3eN%2BeuyYvfRbvlOgleCbLoS7rCIgbRwnRu3xiWQOgcgtm8p8Kqr%2F%2FJLX4hUocJfUE5fcJcJGhJ734w%3A1665885894073; captcha_ticket_v2=2|1:0|10:1665885001|17:captcha_ticket_v2|704:eyJ2YWxpZGF0ZSI6Ik5BTlBfMmNYTnN5T01lRUE0SmhZVk1iTEk5aFdQc25kMGk1cFdFN3RldHhqaUZLTnAyU1dCX3lHU2hsY05INnVoNm4taFFjTmVuVjFKT3FEUTVUcHdpeU5wRWlmemtNQ0M2S1d2RkRqenlrcjdUNGFLcEJCVHlWdlVHdmFESGhJNkJsb3NRa3lYaHhobk9yTVVXZmxxNXlxelpPdUFUZnRfRkdfY0JwLVdORC1vUXBaTEZBbHlyaC4yeDJ2QmlWT1BVN21fTUVpMVl6Z3pMZXhncVdlRktLUkNLQmJnblZsdmstZE93ZEJ1YUZCdEMtV21KMlNPYUlRb2ZVREtFRWF4LnZIWlFZYk9TNS1GYUhONTBmT2tfeUxHTkxWWHh6VXNzd3U2TTVTLnlpc1JRWmtyc1FCMndtLmVtZEFKc0dfa1Atdk5PZlZuSFFkUHFVY3gyaGtMYTZqQ0hfbHYtZXFfNU5uOUV6c2dfV2VSckxVbU8tcGlUd0pLaU5TbDRubzBMVmMuczdtZnNzcUJNYmY3cldUTHdvVFhOUzFTeEtyLVdIdmNWYTlycGJ6WDVmOGxlVC1MMWZKUGhjbmRwdndmTS5TTU1ZOGp0VmZMRmpLdVBSLkJLWThwd1A3RXJJcVBLcVZzQTlielpyNEhCXzVWand4WlI3MmVleV9lanR6MyJ9|c8bbaba4e91a74406513d69a880d66dec8ceaa4266f37e1fe9f7fb5421d759c7; z_c0=2|1:0|10:1665885018|4:z_c0|92:Mi4xbVdiSkd3QUFBQUFBUUZkaHBiTzJGU1lBQUFCZ0FsVk5XckU0WkFCeXFfb1dFVGpmZ1dqRmlFdzRieklkV2NrWmZB|f4ec746b5dc8ae7469ca31a8f4084f9141668ed628e7dbba80d889bd58910d64; NOT_UNREGISTER_WAITING=1; SUBMIT_0=bae63741-46ff-4a67-9f92-4d6957acb938; KLBRSID=b33d76655747159914ef8c32323d16fd|1665889168|1665884977; Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49=1665889173'
    }


    resp = requests.get(url=url,params=param,headers=head)
    content =resp.json()
    content_str = json.dumps(content,ensure_ascii=False)

    # 解析数据
    obj = re.compile(r'"title": "(?P<title>.*?)", "highlight_title":.*?"name": "(?P<class1>.*?)"},.*?"name":.*?"score": (?P<number>.*?),.*?{"url": "(?P<ul>.*?)",',re.S)

    result = obj.finditer(content_str)

    # 保存数据
    f = open('data1.csv','a',encoding='utf-8')

    csvwriter = csv.writer(f)
    
    for it in result:
        dic = it.groupdict()
        csvwriter.writerow(dic.values())


    n += 20

print('over')

