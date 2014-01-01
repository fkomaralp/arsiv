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


def page2filename(page, year):
    """docstring for page2filename"""
    page = page.strip('\n').splitlines()
    body = u''''''
    date = page[:1][0]
    title = page[1:2][0]

    for row in page[1:]:
        body += row + '\n'

    day = date.split(' ')[0]
    month = date.split(' ')[1].strip(',')
    monthindex = aylar.index(month) + 1
    dump2file(year, monthindex, day, body)
    return (date, title, month, day, monthindex)


def dump2file(year, month, day, data):
    """ docstring for dump2file """
    f = open('%s/%s-%s.markdown' %(year, month,day), 'wb', 'utf-8')
    f.write( data )
    return None
