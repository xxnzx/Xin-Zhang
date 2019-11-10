import re
ID=input('请输入十八位身份证号码：')
test=re.compile(r'^\d{17}[\dX]$')
test1=test.match(ID)
if test1:
    print('你的身份证号码是'+ID)
else:
    print('输入的身份证号码错误！')
check_num=0
check_sum=0
weight=[7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]
vaild=[1, 0, 'X', 9, 8, 7, 6, 5, 4, 3, 2]
for i in range(0,17) :
    check_sum+=int(ID[i])*weight[i]
check_num=check_sum%11
if vaild[check_num]==ID[17]:
    print("身份证号码有效！")
else:
    print("身份证号码无效！")
print('您的出生年月日为：'+ID[6:10]+'年'+ID[10:12]+'月'+ID[12:14]+'日')
if int(ID[16])%2==0:
    print("您的性别：女")
else:
    print("您的性别：男")

import os
os.chdir('C://Users//xxnzx//Desktop//')
f=open('city.txt','r')
mylist=list()
for line in f:
    mylist.append(line.split())
print(mylist)
for item in mylist:
    m=re.match('^ID[0:2]0000$',item[0])
    if m:
        province=item[1]
        print(province)
    m1=re.match('^ID[0:4]00$',item[0])
    if m1:
        city=item[1]
        print(city)
    m2=re.match('^ID[0:6]$',item[0])
    if m2:
        county=item[1]
        print(county)


