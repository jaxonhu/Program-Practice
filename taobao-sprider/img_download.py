#coding=utf-8
import re
import requests
import threading
import time
import random as r
url = "https://img11.static.yhbimg.com/goodsimg/2018/09/11/15/013f4f40a8bd6f4d5094a281771c096db7.jpg?imageMogr2/thumbnail/280x382/background/d2hpdGU=/position/center/quality/80"



# img = response.content
# with open("./test.jpg", 'wb') as f:
#     f.write(img)
#     f.close()


main_page = "https://www.yohobuy.com/list/ci52-gd1.html?page="

for i in range(1, 50):
    response = requests.get(main_page + str(i))
    response.encoding = "utf-8"
    content = response.content
    imgs_url = re.findall(r'<img.*data-original="(.*)" alt=.*', content, re.I)
    counter = 0
    for j in range(len(imgs_url)):
        imgurl = re.sub(r'&#x3D;', '=', imgs_url[j], flags=re.I)
        image = requests.get("https:" + imgurl).content
        sleep_time = r.uniform(1, 3)
        time.sleep(sleep_time)
        print "wait..." + str(sleep_time) + " seconds"
        with open("./imgs/" + str(counter) + ".jpg", 'wb') as f:
            f.write(image)
            f.close()
            counter += 1




