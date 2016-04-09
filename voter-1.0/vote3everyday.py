#!/usr/bin/env python
# coding=utf-8

#import sys
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
'13010543189',
'13010573189',
'13012087238',
'13017543189',
'13082341384',
'13087343389',
'13088040384',
'13088341389',
'13088940384',
'13101894238',
'13111894238',
'13130700561',
'13130800561',
'13203784561',
'13213784561',
'13219002579',
'13219082579',
'13219902579',
'13240875931',
'13244875931',
'13246871935',
'13288640901',
'13340870935',
'13346012001',
'13346072001',
'13346772001',
'13348870935',
'13376390811',
'13503704566',
'13503754566',
'13608730931',
'13608770931',
'13646531930',
'13646531931',
'13648730931',
'13686581931',
'13712893238',
'13726201936',
'13726231936',
'13731700561',
'13731900561',
'13731970561',
'13772098215',
'13772498215',
'13812894238',
'13832294238',
'13834002873',
'13834082873',
'13834902873',
'13880580930',
'13884580930',
'13903704561',
'13911093218',
'13911893218',
'13930700564',
'13930701564',
'13931700564',
'13933704564',
'13933790561',
'13976498215',
'13988091388',
'13988391388',
'15012080238',
'15012090238',
'15112014038',
'15190926438',
'15192324438',
'15192926438',
'15212024238',
'15280324238',
'15282324238',
'15289073584',
'15289273584',
'15310017038',
'15312017038',
'15312024238',
'15390724238',
'15392724238',
'15510021238',
'15510028238',
'15512024238',
'15515028238',
'15610907732',
'15610908732',
'15612908732',
'15622008032',
'15712024238',
'15782021238',
'15789021238',
'15812094238',
'15889043221',
'15889083221',
'15889943221',
'15930128238',
'15936128238',
'15966028238',
'16780348176',
'16789943221'
'16789943221',
'17700620923',
'17705620923',
'17745628923',
'17887343389',
'18000335565',
'18003105538',
'18003805538',
'18009335565',
'18112063461',
'18112963461',
'18204900509',
'18207303389',
'18207313389',
'18208900509',
'18280013562',
'18280273584',
'18281013562',
'18289273584',
'18291003510',
'18299403510',
'18333309101',
'18333349101',
'18391003510',
'18398003510',
'18709035565',
'18709335565',
'18783342101',
'18800805538',
'18803805538',
'18832204238',
'18832294238',
'18843278540',
'18880079540',
'18880279540',
'18904000509',
'18904900509',
'18922263461',
'18981013562',
'18981813562',
'19219902579'
]

# Open a file to save those unavailable phone numbers
dirty_phonebook = open("dirty_phonebook.txt", "a")

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
	dict_login = eval(text_login)
	
	# In case to fail to login
	if dict_login["status"] is not 1:
		dirty_phonebook.write(phone + '\n')
		continue

	print("%s" % text_login)

	# Send the HTTP GET REQUEST to vote
	for vote in range(5):
		request_vote = urllib2.Request(vote_url, None, vote_get_header)
		response_vote = urllib2.urlopen(request_vote)
		text_vote = response_vote.read()
		print("%s" % text_vote)

# In the end we keep this dirty phonebook
dirty_phonebook.close()

