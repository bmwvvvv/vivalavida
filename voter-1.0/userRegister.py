#! /usr/bin/env python
# coding = utf-8

import urllib2
import urllib
import cookielib

# phone list
phones = [
    '13178872361',
    '13178872362',
    '13178872363',
    '13178872364',
    '13178872365',
    '13178872366',
    '13178872367',
    '13178872368',
    '13178872369',
    '13178872360'
]

# url which you will register a new user
reg_url = 'http://900.ocarservice.com/index.php/Index/toReg.html'
reg_post_url = 'http://900.ocarservice.com/index.php/Index/saveReg.html'

# construct http header
post_header = {
    'Host': '900.ocarservice.com',
    'Connection': 'keep-alive',
    'Content-Length': '87',
    'Accept': 'application/json',
    'Origin': 'http://900.ocarservice.com',
    'X-Requested-With': 'XMLHttpRequest',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 \
    (KHTML, like Gecko) Chrome/48.0.2564.109 Safari/537.36 OPR/35.0.2066.68',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Referer': 'http://900.ocarservice.com/index.php/Index/toReg.html',
    'Accept-Encoding': 'gzip, deflate, lzma',
    'Accept-Language': 'en-GB,en-US;q=0.8,en;q=0.6'
}

if __name__ == '__main__':
    for phone in phones:
        # setup a cookie processor to download cookie to local
        cookie_jar = cookielib.LWPCookieJar()
        cookie_support = urllib2.HTTPCookieProcessor(cookie_jar)
        opener = urllib2.build_opener(cookie_support, urllib2.HTTPHandler)
        urllib2.install_opener(opener)

        # Open login html so that we can get the cookie
        login_html = urllib2.urlopen(reg_url)

        body = {
            'phone': phone,
            'password': '123456',
            'reuserpwd': '123456',
            'realname': '%E7%8B%84%E5%B0%91%E9%94%8B'
        }

        # Necessary to encode the POST REQUEST
        post_data = urllib.urlencode(body)

        # Send the HTTP POST REQUEST
        request_reg = urllib2.Request(reg_post_url, post_data, post_header)
        response_reg = urllib2.urlopen(request_reg)
        text1 = response_reg.read()
        print("%s" % text1)
