#! /usr/bin/env python
# coding = utf-8

import random

'''
create a Set that holds generated random phone numbers
'''


def gen_phone_numbers(pprefix='138', pnums=1000):
    psuffix_from = 0
    psuffix_to = 99999999
    pset = set([])

    for i in range(pnums):
        pnumber = pprefix + "%08d" % random.randint(psuffix_from, psuffix_to)
        pset.add(pnumber)

    return pset

'''
put these phone numbers into a file
'''


def gen_phone_book(pset):
    PhoneBookFile = 'phonebook.txt'
    pbook = open(PhoneBookFile, 'a+')
    for p in pset:
        pbook.write(p + '\n')
    pbook.close()

if __name__ == '__main__':
    # print gen_phone_numbers(pnums=3)
    gen_phone_book(gen_phone_numbers('136', 200))
    gen_phone_book(gen_phone_numbers('151', 200))
    gen_phone_book(gen_phone_numbers('158', 200))
    gen_phone_book(gen_phone_numbers('152', 200))
    gen_phone_book(gen_phone_numbers('153', 200))
