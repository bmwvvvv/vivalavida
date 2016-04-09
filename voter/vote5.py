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
	'13608730931',
	'13203784561',
	'13101894238',
	'13010543189',
	'12989342771',
	'13880580930',
	'13130800561',
	'13911093218',
	'13988091388',
	'16285049571',
	'13346072001',
	'13731900561',
	'15012080238',
	'16287113382',
	'16780302012',
	'13726201936',
	'13503704566',
	'18832204238',
	'18207313389',
	'18333309101',
	'13l86280811',
	'16255008326',
	'19287604901',
	'18880079540',
	'18112063461',
	'13772098215',
	'13088040384',
	'16780048176',
	'13240875931',
	'17700620923',
	'15610908732',
	'16781249072',
	'13348870935',
	'13930700564',
	'15510028238',
	'15789021238',
	'15390724238',
	'15280324238',
	'15930128238',
	'15190926438',
	'15310017038',
	'16140903561',
	'18398003510',
	'18800805538',
	'18208900509',
	'18280013562',
	'18280273584',
	'18000335565',
	'19270969527',
	'19280910566',
	'19210902579',
	'16830902873',
	'16880943221',
	'18299403510',
	'18003105538',
	'18904000509',
	'18981813562',
	'15289073584',
	'18709035565',
	'16277069527',
	'16289010566',
	'13219002579',
	'13834002873',
	'15889043221'
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
