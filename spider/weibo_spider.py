#!/usr/bin/python
# *-*coding:utf8*-*

import re
import sys
import os
import urllib2
from bs4 import BeautifulSoup
import requests
from lxml import etree

reload(sys)
sys.setdefaultencoding('utf8')
if len(sys.argv) >= 2:
    user_id = int(sys.argv[1])
else:
    user_id = int(raw_input(u"Please input your user_id:"))

cookie = {"Cookie": "_T_WM=ec00ddcffd420bc54af532fbb5e95dd4; \
          SUB=_2A2578W58DeTxGeRG7FYX8y7Kwj6IHXVZGnI0rDV6PUJbr\
          dANLWbwkW1LHeuhZhrbGFSFCkOpSooMxrNoIrm8dg..; SUHB=0\
          u5BbirEHSX2Ca; SSOLoginState=1458904620"}
url = "http://weibo.cn/u/%d?filter=1&page=1" % user_id

html = requests.get(url, cookies=cookie).content
selector = etree.HTML(html)
pageNum = int(selector.xpath('//input[@name="mp"]')[0].attrib['value'])
print "Capture %d pages" % pageNum

result = ""
urllist_set = set()
word_count = 1
image_count = 1
x = 1


print "Spider ready! Go"

for page in range(1, pageNum+1):
    # retrieve the lxml pages
    url = 'http://weibo.cn/u/%d?filter=1&page=%d' % (user_id, page)
    lxml = requests.get(url, cookies=cookie).content

    # retrieve the text
    selector = etree.HTML(lxml)
    content = selector.xpath('//span[@class="ctt"]')
    for each in content:
        text = each.xpath('string(.)')
        if word_count >= 4:
            text = "%d:" % (word_count-3) + text + "\n\n"
        else:
            text = text + "\n\n"
        result = result + text
        word_count += 1

    fo = open("%d" % user_id, "wb")
    fo.write(result)
    fo.write("finish retrieving the %sth page text\n\n" % page)
    fo.close()
    word_path = os.getcwd() + "%d" % user_id

    # retrieve the images
    soup = BeautifulSoup(lxml, "lxml")
    urllist = soup.find_all('a', href=re.compile(r'^http://weibo.cn/mblog/oripic', re.I))
    first = 0
    for imgurl in urllist:
        urllist_set.add(requests.get(imgurl['href'], cookies=cookie).url)
        image_count += 1

    if not urllist_set:
        print "No images in this page"
    else:
        image_path = os.getcwd() + '/weibo_image'
        if os.path.exists(image_path) is False:
            os.mkdir(image_path)
        for imgurl in urllist_set:
            temp = image_path + '/%s.jpg' % x
            print "The %sth image downloading ..." % x
            try:
                real_url = urllib2.urlopen(imgurl).geturl()
                url = str(real_url)
                req = urllib2.Request(url)
                resp = urllib2.urlopen(req)
                resp_html = resp.read()
                bin_file = open(temp, "wb")
                bin_file.write(resp_html)
                bin_file.close()
            except:
                print "Failed to download this image: %s" % imgurl
            x += 1

print "finish spidering weibo, total %d items, save to %s" % (word_count-4, word_path)
print "finish spidering images, total %d images, save to %s" % (image_count-1, image_path)
