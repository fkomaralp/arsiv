#!/usr/bin/env python
# -*- coding: utf-8 -*-

from codecs import open

aylar = [u'Ocak',
         u'Şubat',
         u'Mart',
         u'Nisan',
         u'Mayıs',
         u'Haziran',
         u'Temmuz',
         u'Ağustos',
         u'Eylül',
         u'Ekim',
         u'Kasım',
         u'Aralık']

f = open('_log.log', 'wb', 'utf-8')

def page2filename(page):
    """docstring for page2filename"""
    page = page.strip('\n').splitlines()
    body = u''''''
    date = page[:1][0]
    title = page[2:3][0]
    #for row in page[1:]:
    #    body += row

    day = date.split(' ')[0]
    month = date.split(' ')[1].strip(',')
    monthindex = aylar.index(month) + 1
    return (date, title, month, day, monthindex )
