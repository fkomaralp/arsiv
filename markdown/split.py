#!/usr/bin/env python
# -*- coding: utf-8 -*-

from libsplit import page2filename

def main():
    """docstring for split"""
    from codecs import open
    yillar = [ y for y in range(1989,1998) if y != 1993 ]
    for i in yillar:
        f = open('%s.markdown' %i, 'rb', 'utf-8')
        year = f.read().split('---')
        year.pop(0)
        for page in year:
            date, title, month, day, mind = page2filename(page)
            #import ipdb; ipdb.set_trace()
            #if len(title) == 0 or len(month) == 0 or len(day) == 0:
            print u'Yıl: %s Ay: %s\tGün: %s | Başlık: %s' %(i, month, day,title)
if __name__ == '__main__':
    main()
