#!/usr/bin/env python
# coding=utf-8

import urllib2
import urllib
import urlparse
import HTMLParser
import cookielib
import string
import re

# url which you will login
login_url = 'http://900.ocarservice.com/index.php/Index/tologin.html'
post_url = 'http://900.ocarservice.com/index.php/Index/login.html'

# setup a cookie processor to download cookie to local
cookie_jar = cookielib.CookieJar()
cookie_support = urllib2.HTTPCookieProcessor(cookie_jar)
opener = urllib2.build_opener(cookie_support, urllib2.HTTPHandler)
urllib2.install_opener(opener)

# Open login html so that we can get the cookie
login_html = urllib2.urlopen(login_url)

# construct http header
header = {
	'Content-Length' : '36',
	'Accept' : '*/*',
	'Origin' : 'http://900.ocarservice.com',
	'X-Requested-With' : 'XMLHttpRequest',
	'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.109 Safari/537.36 OPR/35.0.2066.68',
	'Content-Type' : 'application/x-www-form-urlencoded',
	'Referer' : 'http://900.ocarservice.com/index.php/Index/tologin.html',
	'Accept-Encoding' : 'gzip, deflate, lzma',
	'Accept-Language' : 'en-GB,en-US;q=0.8,en;q=0.6'
}

body = {
	'nickname' : '13100091236',
	'password' : '123456'
}
# body = {
# 	'nickname' : '18792851236',
# 	'password' : '963852741'
# }

# Necessary to encode the POST REQUEST
post_data = urllib.urlencode(body)


# Send the HTTP POST REQUEST
request = urllib2.Request(post_url, post_data, header)
print("%s" % request)
response = urllib2.urlopen(request)
text = response.read()
print("%s" % text)
