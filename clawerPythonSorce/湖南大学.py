#!/usr/bin/python3
#coding=utf-8
import requests
import json
import logging
import os
import xlwt
json_url = 'https://hnu.bysjy.com.cn/module/getcareers?start_page=1&keyword=&type=inner&day=&count=15&start=1&_=1536044186160'
logging.basicConfig(level=logging.DEBUG,format='')

json_data = requests.get(json_url)
#print(json_data.text)

workbook = xlwt.Workbook()
sheet1 = workbook.add_sheet('list1')
sheet1.write(0,0,'ʱ��')
sheet1.write(0,1,'�ص�')
sheet1.write(0,2,'��˾����')
sheet1.write(0,3,'��Ƹ��')
sheet1.write(0,4,'רҵҪ��')
sheet1.write(0,6,'��ϸ��Ϣ')
count=1
    
data_list = json_data.json()['data']#the useful data 

for i in data_list:
        sheet1.write(count,0,i['meet_day']+i['meet_time'])
        sheet1.write(count,1,i['address'])
        sheet1.write(count,2,i['company_name'])
        sheet1.write(count,3,i['meet_name'])
        sheet1.write(count,4,i['professionals'])
        sheet1.write(count,5,'https://hnu.bysjy.com.cn/detail/career?id='+i['career_talk_id'])
        count=count+1
workbook.save('���ϴ�ѧ��Ƹ��Ϣ.xlsx')