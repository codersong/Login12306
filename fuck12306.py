# utf-8 __*__
import requests
import re
from bs4 import BeautifulSoup
import random
import urllib,urllib3
from PIL import Image
import matplotlib.pyplot as plt
from io import BytesIO

import sys
import time

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64)\
    AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.118 Safari/537.36', }
def getPassengerUrl():

    '''获取客运服务URL地址'''
    url_12306 = "http://www.12306.cn/mormhweb/"

    r = requests.get(url_12306, headers=headers)
    soup = BeautifulSoup(r.text.encode(r.encoding).decode('utf-8'), 'lxml')
    tag_a = soup.find_all('a')
    dict = {}
    for a in tag_a:
        dict.update({a.string:a['href']})
    return dict[u'客运服务']



url_dict = {
    'passport_login': 'https://kyfw.12306.cn/passport/web/login',
    'passport_captcha': 'https://kyfw.12306.cn/passport/captcha/captcha-image',
    'passport_authuam': 'https://kyfw.12306.cn/passport/web/auth/uamtk',
    'passport_captcha_check': 'https://kyfw.12306.cn/passport/captcha/captcha-check',
    'passport_query': 'https://kyfw.12306.cn/otn/leftTicket/query?',
}

station_name = {
    u'驻马店': 'ZDN',
    u'信阳东': 'OYN',
    u'深圳': 'SZQ',
    u'广州南': 'IZQ'
}

passenger_date = ['2018-08-31']


query_header = {
    'Accept': '*/*',
    'Accept-Encoding': "gzip, deflate, sdch, br",
    'Accept-Language': "zh-CN,zh;q=0.8",
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Cookie': 'JSESSIONID=95306A8E7B875745757827DDC7439A40; route=6f50b51faa11b987e576cdb301e545c4; BIGipServerotn=2597781770.50210.0000; RAIL_EXPIRATION=1535781862859; RAIL_DEVICEID=hxPrei-7if4iUd40f2RmSDNpMhIXOzQa7i5kP0THYFY5rYA6kYcAmJ_6bY858nt-X8CwUIek7CGuPtSVjVetb79Zp3g4M-W2J8Zd2Jt1o3_ZrBiTjhW61ctbd-R32qg8x5bQZuVYABcHXQuZci9VaUwHELU7OzFK; _jc_save_fromStation=%u6DF1%u5733%2CSZQ; _jc_save_toStation=%u4FE1%u9633%u4E1C%2COYN; _jc_save_fromDate=2018-08-31; _jc_save_toDate=2018-08-29; _jc_save_wfdc_flag=dc',
    'If-Modified-Since': '0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
    'X-Requested-With': "XMLHttpRequest",

}

def getPassportQueryUrl(start, stop, date):
    return url_dict['passport_query'] + 'leftTicketDTO.train_date=' + date + '&leftTicketDTO.from_station=' + start + '&leftTicketDTO.to_station='+ stop + '&purpose_codes=ADULT'
query_response = []
for date in passenger_date:
    url = getPassportQueryUrl(station_name[u'驻马店'], station_name[u'深圳'], date)
    query_response.append(requests.get(url,headers=query_header).text)
    time.sleep(5)
    print(url)
tick_info = {
        'number3': '',
        'start_time8': '',
        'stop_time9': '',
        'duration10': '',
        'VIP_seat32': '',
        'first_seat31': '',
        'second_seat30': '',
        'dongwo28': '',
        'yingwo27': '',
        'ruanzuo26': '',
        'yingzuo25': '',
        'wuzuo24': '',
        'qita23': ''
    }
for result in query_response:
    for i in result.split(','):
        if i.find('|') !=-1:
            print(i.split('|'))
            print(len(i.split('|')))







