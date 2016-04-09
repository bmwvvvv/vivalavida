#!/usr/bin/env python
#-*- coding: utf-8 -*-

import urllib2
from threading import Thread
from time import time

class Vote(Thread):
	def __init__(self, proxy):
		Thread.__init__(self)
		self.proxy = proxy
		self.url = 'http://900.ocarservice.com/index.php/
					Event/toViewSign.html?id=195'
		self.timeout = 10
	
	def run(self):
		proxy_handle = urllib2.ProxyHandler({"http":
					r'http://%s' % self.proxy})
		opener = urllib2.build_opener(proxy_handle)
		urllib2.install_opener(opener)
		try:
			response = urllib2.urlopen(self.url, timeout=
									self.timeout)
			result = response.read().decode('gbk')
			print result
			pos = result.find(u'')
			if pos > 1:
				addnum()
			else:
				pass
		except Exception, e:
			print e.message, 'error'

def addnum():
	global n
	n += 1

def shownum():
	return n

n = 0
threads = []
proxylist = open('', 'r')

for proxy in proxylist:
	t = Vote(proxy)
	threads.append(t)

if __name__ == '__main__':
	start_time = time()
	for i in threads:
		i.start()
	for i in threads:
		i.join()
	
