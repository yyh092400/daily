import csv
# with open('C:\\Users\suhong\\Desktop\\test.csv','r',encoding='utf-8') as f:
#     re=csv.DictReader(f)
#     with open('name.txt','a+',encoding='utf-8') as y:
#         # xe=open('name.txt','a+')
#         for i in re:
#             y.write(str(i)+'\n')
#         y.seek(0)
#         print(y.read())
#第一题！！！
##把学号,姓名,平时成绩,期末成绩，   转换成字典格式{'1445204009': '王召', '100': '96'}
####1445204009,王召,100,90
with open('C:\\Users\suhong\\Desktop\\test.csv','r',encoding='utf-8') as f:
    re = csv.DictReader(f)
    a={}
    for i in re:
        a[i['学号']] = i['姓名']
        a[i['平时成绩']] = i['期末成绩']
    print(a)
