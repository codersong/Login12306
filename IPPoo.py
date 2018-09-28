# utf-8 __*__
import requests
import re
from bs4 import BeautifulSoup
import time
import random
import urllib,urllib3
from PIL import Image
import matplotlib.pyplot as plt
from io import BytesIO
import sys
test_url = 'https://www.baidu.com/'
ip_url = 'http://www.xicidaili.com/'
captcha_12306 = 'https://kyfw.12306.cn/passport/captcha/captcha-image'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64)\
    AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.118 Safari/537.36', }
ip_response = requests.get(ip_url,headers = headers).text
ip_soup = BeautifulSoup(ip_response,'lxml')
#print(ip_soup)

tag_tr = ip_soup.find_all('tr')
IPPool = []

for tr in tag_tr:
    ip_info = {
        'ip1': '',
        'port2': '',
        'location3': '',
        'type5': '',
        'live_time6': '',
        'verify_time7': ''
    }
    if len(tr.find_all('td')) == 8:
        #print(tr.find_all('td')[1].contents[0])
        try:
            #print(tr.find_all('td'))
            ip_info['ip1'] = tr.find_all('td')[1].contents[0]
            ip_info['port2'] = tr.find_all('td')[2].contents[0]
            ip_info['location3'] = tr.find_all('td')[3].contents[0]
            ip_info['type5'] = tr.find_all('td')[5].contents[0]
            ip_info['live_time6'] = tr.find_all('td')[6].contents[0]
            ip_info['verify_time7'] = tr.find_all('td')[7].contents[0]
            IPPool.append(ip_info)
        except:
            pass
print(IPPool)
for ip in IPPool:
    proxies = {
        'http': 'https://'+ip['ip1']
    }
    print(proxies)
    try:
        r = requests.get(captcha_12306, headers=headers, proxies=proxies,timeout = 5)
        print(r.status_code)
        image = Image.open(BytesIO(r.content))
        image.save(r'F:\\12306\\' + time.strftime("%Y%m%d %H%M%S",time.localtime()) + '.png')
        #image.show()
        time.sleep(5)
    except:
        #print("******")
        pass




