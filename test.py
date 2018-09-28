# utf-8 __*__
import os
import pytesseract
import base64
import numpy as np
cmd = "tesseract F:\\python\\data\\title.png  F:\\python\\data\\1.txt -l chi_sim "
import cv2 as cv
import urllib.parse
#os.system(cmd)
from PIL import Image

#image = Image.open('F:\\python\\data\\title.png')
#print(image)
#code = pytesseract.image_to_string(image, lang='chi_sim')
#print(code)
import requests
import json

img_file = open('F:\\python\\data\\title.png', 'rb')
img_b664encode = base64.b64encode(img_file.read())
img_file.close()
print(img_b664encode)
img = base64.b64decode(img_b664encode)
img_array = np.fromstring(img, np.uint8)
img = cv.imdecode(img_array, cv.COLOR_BGR2RGB)
cv.imshow('img',img)
cv.waitKey(0)
cv.destroyAllWindows()
img_urlencode = urllib.parse.quote(img_b664encode)
print(img_urlencode)


API_key = 'HLXWEwmcaBHHeCqS4gekuGbV'
Secret_key = 'eu45PtnAWhzELCcEhRZTrahhVz5MxRML'
get_token_url = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&' +  'client_id=' + API_key + '&client_secret=' +Secret_key

r = requests.post(get_token_url)
print(json.loads(r.text)['access_token'])


