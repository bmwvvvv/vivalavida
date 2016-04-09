#!/usr/bin/env python
# coding=utf-8

import urllib2
import urllib
import urlparse
import HTMLParser
import cookielib
import string
import re

# url to register a user
# url which you will login
login_url = 'http://900.ocarservice.com/index.php/Index/tologin.html'
login_post_url = 'http://900.ocarservice.com/index.php/Index/login.html'

# url to vote
vote_url = 'http://900.ocarservice.com/index.php/Event/toVote/id/195.html'

# url which you will register a new user
reg_url = 'http://900.ocarservice.com/index.php/Index/toReg.html'
reg_post_url = 'http://900.ocarservice.com/index.php/Index/saveReg.html'

# phone list
phones = [
	'13646531931',
	'13933784561',
	'13812894238',
	'13087343389',
	'16988342171',
	'13686581931',
	'13933790561',
	'13712893238',
	'13088341389',
	'16788349171',
	'13246871931',
	'13933784561',
	'15812094238',
	'16887303389',
	'16980342111',
	'13646531930',
	'13903704561',
	'13832294238',
	'17887343389',
	'18783342101',
	'13376390811',
	'16355098326',
	'13288640901',
	'18843278540',
	'18922263461',
	'13976498215',
	'13082341384',
	'16787349176',
	'13246871931',
	'17745628923',
	'15622008032',
	'16788249172',
	'13246871935',
	'13933704564',
	'15512024238',
	'15712024238',
	'15312024238',
	'15212024238',
	'15966028238',
	'15192324438',
	'15112014038',
	'19202903561',
	'19309903510',
	'19809803538',
	'19304903509',
	'19181513562',
	'19209203584',
	'19009305565',
	'19507909527',
	'19389900566',
	'19409902579',
	'16634902873',
	'16789943221'
]

# construct http header
reg_post_header = {
	'Host' : '900.ocarservice.com',
	'Connection' : 'keep-alive',
	'Content-Length' : '87',
	'Accept' : 'application/json',
	'Origin' : 'http://900.ocarservice.com',
	'X-Requested-With' : 'XMLHttpRequest',
	'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.109 Safari/537.36 OPR/35.0.2066.68',
	'Content-Type' : 'application/x-www-form-urlencoded',
	'Referer' : 'http://900.ocarservice.com/index.php/Index/toReg.html',
	'Accept-Encoding' : 'gzip, deflate, lzma',
	'Accept-Language' : 'en-GB,en-US;q=0.8,en;q=0.6'
}

# construct http header
# For login
login_post_header = {
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

# For vote
vote_get_header = {
	'Host' : '900.ocarservice.com',
	'Connection' : 'keep-alive',
	'Accept' : 'application/json, text/javascript, */*; q=0.01',
	'X-Requested-With' : 'XMLHttpRequest',
	'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.109 Safari/537.36 OPR/35.0.2066.68',
	'Referer' : 'http://900.ocarservice.com/index.php/Event/toViewSign.html?id=195',
	'Accept-Encoding' : 'gzip, deflate, lzma, sdch',
	'Accept-Language' : 'en-GB,en-US;q=0.8,en;q=0.6'
}

for phone in phones:

	# setup a cookie processor to download cookie to local
	cookie_jar = cookielib.LWPCookieJar()
	cookie_support = urllib2.HTTPCookieProcessor(cookie_jar)
	opener = urllib2.build_opener(cookie_support, urllib2.HTTPHandler)
	urllib2.install_opener(opener)

	# Login to register html and get the cookie
	reg_html = urllib2.urlopen(reg_url)


	reg_body = {
		'phone' : phone,
		'password' : '123456',
		'reuserpwd' : '123456',
		'realname' : '%E7%8B%84%E5%B0%91%E9%94%8B'
	}

	# Necessary to encode the POST REQUEST
	reg_post_data = urllib.urlencode(reg_body)

	# Send the HTTP POST REQUEST
	request_reg = urllib2.Request(reg_post_url, reg_post_data, reg_post_header)
	response_reg = urllib2.urlopen(request_reg)
	text_reg = response_reg.read()
	print("%s" % text_reg)

	# Open login html so that we can get the cookie
	login_html = urllib2.urlopen(login_url)


	login_body = {
		'nickname' : phone,
		'password' : '123456'
	}

	# Necessary to encode the POST REQUEST
	login_post_data = urllib.urlencode(login_body)


	# Send the HTTP POST REQUEST to login
	request_login = urllib2.Request(login_post_url, login_post_data, login_post_header)
	response_login = urllib2.urlopen(request_login)
	text_login = response_login.read()
	print("%s" % text_login)

	# Send the HTTP GET REQUEST to vote
	for vote in range(5):
		request_vote = urllib2.Request(vote_url, None, vote_get_header)
		response_vote = urllib2.urlopen(request_vote)
		text_vote = response_vote.read()
		print("%s" % text_vote)
