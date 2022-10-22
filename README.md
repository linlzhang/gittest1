# 复试
**用来提交复试**


## 4.1 开启省流模式

#### 依赖项
pip install request

pip install re

pip install csv

pip install wordcloud

#### 使用方法
设定时间，运行zhihurebang.py

得到知乎小时榜的前100条热点信息

包括每一条热点的标题，热点分类，热力值，链接

终端输出'over'表示程序执行完毕

保存到data1.csv文件中

同时每隔1小时会继续执行程序得到新的数据



运行zhihurebangciyun.py

得到当前小时榜上前100条热点信息的分类

并生成词云

保存到zhihurebang.png

#### 测试截图
打开zhihurebang.py

![屏幕截图_20221022_122834](https://user-images.githubusercontent.com/113598813/197319110-59f98a89-2db2-4d98-9d63-40f2e1fe59e3.png)’

在此处设定程序开始时间

![屏幕截图_20221022_123132](https://user-images.githubusercontent.com/113598813/197319808-f3321794-e8a3-48c4-8552-8f8379c81e53.png)

运行程序，显示程序执行所需时间

![屏幕截图_20221022_123220](https://user-images.githubusercontent.com/113598813/197319822-a6c90d3c-61a0-403a-9aa9-8f0be41a03b8.png)

显示'over'和程序下一次执行时间，运行成功！

![屏幕截图_20221022_123607](https://user-images.githubusercontent.com/113598813/197319918-dcb5e915-2c70-4a0c-b299-494354e0b492.png)

打开data1.csv看到被保存的数据

![屏幕截图_20221022_123903](https://user-images.githubusercontent.com/113598813/197320010-1b8e94e4-a383-4fcf-9005-8bafbd25ddf6.png)

输入ctrl+c即可结束程序


打开zhihurebangciyun.py

同样设定程序开始时间和运行程序

显示'over'和下一次执行所需时间

![屏幕截图_20221022_124554](https://user-images.githubusercontent.com/113598813/197320230-d7a69d7a-b7c8-4105-8b1a-35304505d2bd.png)

打开zhihurebang.png看到生成的词云图

同样结束程序


## 4.2 查查成分

#### 依赖项
pip install request

pip install re

pip install csv

#### 使用方法
设定两个已知的uid

运行bzhanguanzhu.png

显示'over'表示程序运行结束

得到两个用户前100个关注(能显示的最大数量)中的共同关注

以及这些账号的粉丝数，UID，用户昵称，等级

保存到data2.csv中

#### 测试截图
打开bzhanguanzhu.py

![屏幕截图_20221022_125843](https://user-images.githubusercontent.com/113598813/197320679-58ebd4a8-99c6-41c7-95a1-342f1dcaf58e.png)

在'vmid'处输入想要查询的两个uid

![屏幕截图_20221022_125236](https://user-images.githubusercontent.com/113598813/197320708-3ddb7410-0cd7-4041-9831-98628d001609.png)

显示'over'表示程序运行成功！

![屏幕截图_20221022_130104](https://user-images.githubusercontent.com/113598813/197320736-b6d31253-a292-4095-9ab3-a8533bb6b30f.png)

打开data2.csv，看到数据



## 4.3 等通知！

#### 依赖项
pip install request

pip install re

pip install csv

#### 使用方法
设定时间，运行benkeshengtongzhi.py

得到官网上的前150条通知数据

包括通知标题，发布时间，链接

保存到data3.csv中

同时每隔一天会自动执行程序

#### 测试截图
打开benkeshengtongzhi.py

设置时间，运行结果，结束方式均同4.1

![屏幕截图_20221022_131417](https://user-images.githubusercontent.com/113598813/197321778-ac5f54a4-e617-457e-a06c-1799e95af864.png)

打开data3.csv，看到数据
