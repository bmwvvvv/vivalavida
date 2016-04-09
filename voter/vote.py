#!/usr/bin/python
# coding=utf-8

import time
import urllib2
import urllib
import cookielib
import platform

'''
Something dependent platform
'''

if platform.system() == 'Windows':
	dir_path = r'e:\projects\py_test\voter\\'
else:
	dir_path = r'/home/c/voter/'

# url to register a user
# url which you will login
login_url = 'http://900.ocarservice.com/index.php/Index/tologin.html'
login_post_url = 'http://900.ocarservice.com/index.php/Index/login.html'

# url to vote
vote_url = 'http://900.ocarservice.com/index.php/Event/toVote/id/195.html'

# get usernames
dirty_phonebook = open(dir_path+"registeredPhoneBook.txt", "r")
phones = dirty_phonebook.readlines()
dirty_phonebook.close()

# construct http header
# For login
login_post_header = {
    'Content-Length': '36',
    'Accept': '*/*',
    'Origin': 'http://900.ocarservice.com',
    'X-Requested-With': 'XMLHttpRequest',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 \
    (KHTML, like Gecko) Chrome/48.0.2564.109 Safari/537.36 OPR/35.0.2066.68',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Referer': 'http://900.ocarservice.com/index.php/Index/tologin.html',
    'Accept-Encoding': 'gzip, deflate, lzma',
    'Accept-Language': 'en-GB,en-US;q=0.8,en;q=0.6'
}

# For vote
vote_get_header = {
    'Host': '900.ocarservice.com',
    'Connection': 'keep-alive',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'X-Requested-With': 'XMLHttpRequest',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 \
    (KHTML, like Gecko) Chrome/48.0.2564.109 Safari/537.36 OPR/35.0.2066.68',
    'Referer': 'http://900.ocarservice.com/index.php/Event/toViewSign.html?\
    id=195',
    'Accept-Encoding': 'gzip, deflate, lzma, sdch',
    'Accept-Language': 'en-GB,en-US;q=0.8,en;q=0.6'
}


if __name__ == '__main__':
    # log
    logfile = open(dir_path+"vote.log", "a+")

    login_fail_nums = 0
    vote_num = 0

    # begin to tick (CPU time)
    time.clock()
    # record the elapsed time
    start_time = time.ctime()

    for phone in phones:

        # setup a cookie processor to download cookie to local
        cookie_jar = cookielib.LWPCookieJar()
        cookie_support = urllib2.HTTPCookieProcessor(cookie_jar)
        opener = urllib2.build_opener(cookie_support, urllib2.HTTPHandler)
        urllib2.install_opener(opener)

        # Open login html so that we can get the cookie
        login_html = urllib2.urlopen(login_url)

        login_body = {
            'nickname': phone,
            'password': '123456'
        }

        # Necessary to encode the POST REQUEST
        login_post_data = urllib.urlencode(login_body)

        # Send the HTTP POST REQUEST to login
        request_login = urllib2.Request(login_post_url, login_post_data,
                                        login_post_header)
        response_login = urllib2.urlopen(request_login)
        text_login = response_login.read()
        dict_login = eval(text_login)

        # In case to fail to login
        if dict_login["status"] != 1:
            login_fail_nums += 1
            print "Currently %d users login fail!" % login_fail_nums
            continue

        # Send the HTTP GET REQUEST to vote
        for vote in range(5):
            request_vote = urllib2.Request(vote_url, None, vote_get_header)
            response_vote = urllib2.urlopen(request_vote)
            dict_vote = eval(response_vote.read())
            if dict_vote["status"] == 1:
                vote_num += 1
    # report the elapsed time
    end_time = time.ctime()
    """
    print "The event started at %s." % start_time
    print "The event ended at %s." % end_time
    print "The elapsed time is %f seconds." % time.clock()
    """

    logfile.write("The event started at %s.\n\n" % start_time)
    logfile.write("The event ended at %s.\n" % end_time)
    logfile.write("The elapsed time is %f seconds.\n" % time.clock())
    logfile.write("%s %d vote completed.\n\n" % (time.ctime(),
                                               vote_num))

    logfile.close()
