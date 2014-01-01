#!/usr/bin/env python
# -*- coding: utf-8 -*-

from libsplit import page2filename
import codecs

logs = codecs.open('_log.log', 'w', 'utf-8')

def main():
    "docstring for split"""
    from codecs import open
    yillar = [ y for y in range(1989,1998) if y != 1993 ]
    #for yil in [1989]:
    for yil in yillar:
        total = 0
        f = open('%s.markdown' %yil, 'rb', 'utf-8')
        year = f.read().split('---')
        year.pop(0)
        for page in year:
        #for page in year[:1]:
            date, title, month, day, mind = page2filename(page, yil)
            #if len(title) == 0 or len(month) == 0 or len(day) == 0:
            data = u'%s |  %s %s \t | %s' \
                    %(yil, day, month, title)
            logs.write( data + '\n')
            #print data
if __name__ == '__main__':
    main()
