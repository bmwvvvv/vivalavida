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

# phone list
phones = [
	'13648730931',
	'13213784561',
	'13111894238',
	'13017543189',
	'12980342771',
	'13884580930',
	'13130700561',
	'13911893218',
	'13988391388',
	'16285349571',
	'13346772001',
	'13731700561',
	'15012090238',
	'16287103382',
	'16780342012',
	'13726231936',
	'13503754566',
	'18832294238',
	'18207303389',
	'18333349101',
	'13l86290811',
	'16255098326',
	'19287644901',
	'18880279540',
	'18112963461',
	'13772498215',
	'13088940384',
	'16780348176',
	'13244875931',
	'17705620923',
	'15612908732',
	'16780249072',
	'13340870935',
	'13931700564',
	'15515028238',
	'15782021238',
	'15392724238',
	'15282324238',
	'15936128238',
	'15192926438',
	'15312017038',
	'16142903561',
	'18391003510',
	'18803805538',
	'18204900509',
	'18281013562',
	'18289273584',
	'18009335565',
	'19277969527',
	'19289910566',
	'19219902579',
	'16834902873',
	'16889943221',
	'18291003510',
	'18003805538',
	'18904900509',
	'18981013562',
	'15289273584',
	'18709335565',
	'16277969527',
	'16289910566',
	'13219902579',
	'13834902873',
	'15889943221'
]

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
