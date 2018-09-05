#!/usr/bin/python3
#coding=utf-8
import requests
import json
import logging
import os
import xlwt
basic_url = 'http://jobs.xtu.edu.cn/index/getdaycareers?day=2018-10-'
logging.basicConfig(level=logging.DEBUG,format='')

workbook = xlwt.Workbook()
sheet1 = workbook.add_sheet('list1')
sheet1.write(0,0,'ʱ��')
sheet1.write(0,1,'�ص�')
sheet1.write(0,2,'��˾����')
sheet1.write(0,3,'רҵҪ��')
sheet1.write(0,5,'��ϸ��Ϣ')
count=1
for i in range(1,32):
    url = basic_url+str(i)
    logging.debug('the clawer web site is:'+url)
    clawertext = requests.get(url)
    logging.debug(type(clawertext))
    logging.debug(clawertext.json())
    logging.debug(clawertext.json()['data'])
    logging.debug(type(clawertext.json()['data']))
    
    data_list = clawertext.json()['data']#the useful data 

    for i in data_list:
        sheet1.write(count,0,i['meet_day'])
        sheet1.write(count,1,i['address'])
        sheet1.write(count,2,i['meet_name'])
        sheet1.write(count,3,i['professionals'])
        sheet1.write(count,5,'http://jobs.xtu.edu.cn/detail/career?id='+i['career_talk_id'])
        count=count+1
workbook.save('��̶��ѧʮ�·���Ƹ��Ϣ.xlsx')