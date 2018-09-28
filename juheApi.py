import requests
import re
from bs4 import BeautifulSoup
import random
import urllib,urllib3
from PIL import Image
import matplotlib.pyplot as plt
from io import BytesIO

login_url = "https://accounts.douban.com/login"
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64)\
AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.118 Safari/537.36',}

my_post = {'redir':'https://www.douban.com/',
           'form_email':'965791303@qq.com',
           'form_password':'song3.1415926',
           'login':'登录'}
r = requests.post(login_url,data = my_post,headers = headers)
html = r.text
#print(html)
soup = BeautifulSoup(html,"lxml")
taglist = soup.find_all(name='img',class_='captcha_image')
captcha_imge_url=''
for tag in taglist:
    captcha_imge_url = tag['src']
print(captcha_imge_url)
img = Image.open(BytesIO(requests.get(captcha_imge_url).content))
plt.imshow(img)
plt.show()
captcha = input('captcha is:')

regid = r'<input type="hidden" name="captcha-id" value="(.*?)"/>'
ids = re.findall(regid, html)
my_post["captcha-solution"]=captcha
my_post["captcha-id"]=ids[0]
print(ids)
q= requests.post(login_url,data=my_post,headers=headers)
print(q.url)
if q.url=='https://www.douban.com/':
    print("登录成功")
html = q.text
soup = BeautifulSoup(html,'lxml')
print(soup)
