import requests
import re
import os
from bs4 import BeautifulSoup

headers={'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"}
all_url="http://www.58pic.com/piccate/10-0-0.html"
start_html=requests.get(all_url,headers=headers).text
#soup=BeautifulSoup(start_html.text,"lxml")
#all_img=soup.find('div',class_="main-left fl").find_all('img')
all_img=re.findall(r'data-original="(.*?)"',start_html,re.S)
i=0
for each in all_img:
    print(each)
    i += 1
    try:
        img = requests.get(each, timeout=10)
    except BaseException as e:
        print(e)
        print('当前图片下载错误')
        continue
    string="F:/asd/"+str(i)+".jpg"
    with open(string,'wb') as f:
        f.write(img.content)
        f.close()
    print("下载完成")




print('总共有%s' %(i)+"张图片")