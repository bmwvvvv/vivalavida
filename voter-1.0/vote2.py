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

# url to vote
vote_url = 'http://900.ocarservice.com/index.php/Event/toVote/id/195.html'

# setup a cookie processor to download cookie to local
cookie_jar = cookielib.LWPCookieJar()
cookie_support = urllib2.HTTPCookieProcessor(cookie_jar)
opener = urllib2.build_opener(cookie_support, urllib2.HTTPHandler)
urllib2.install_opener(opener)

# Open login html so that we can get the cookie
login_html = urllib2.urlopen(login_url)

# construct http header
# For login
post_header = {
	'Content-Length' : '39',
	'Accept' : '*/*',
	'Origin' : 'http://900.ocarservice.com',
	'X-Requested-With' : 'XMLHttpRequest',
	'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.109 Safari/537.36 OPR/35.0.2066.68',
	'Content-Type' : 'application/x-www-form-urlencoded',
	'Referer' : 'http://900.ocarservice.com/index.php/Index/tologin.html',
	'Accept-Encoding' : 'gzip, deflate, lzma',
	'Accept-Language' : 'en-GB,en-US;q=0.8,en;q=0.6'
}

# For vote
get_header = {
	'Host' : '900.ocarservice.com',
	'Connection' : 'keep-alive',
	'Accept' : 'application/json, text/javascript, */*; q=0.01',
	'X-Requested-With' : 'XMLHttpRequest',
	'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.109 Safari/537.36 OPR/35.0.2066.68',
	'Referer' : 'http://900.ocarservice.com/index.php/Event/toViewSign.html?id=195',
	'Accept-Encoding' : 'gzip, deflate, lzma, sdch',
	'Accept-Language' : 'en-GB,en-US;q=0.8,en;q=0.6'
}

body = {
	'nickname' : '13100091235',
	'password' : '123456'
}

# Necessary to encode the POST REQUEST
post_data = urllib.urlencode(body)


# Send the HTTP POST REQUEST
request_login = urllib2.Request(post_url, post_data, post_header)
print("%s" % request_login)
response_login = urllib2.urlopen(request_login)
text1 = response_login.read()
print("%s" % text1)

# Send the HTTP GET REQUEST
request_vote = urllib2.Request(vote_url, None, get_header)
print("%s" % request_vote)
response_vote = urllib2.urlopen(request_vote)
text2 = response_vote.read()
print("%s" % text2)
