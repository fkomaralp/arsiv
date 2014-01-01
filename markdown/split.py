#!/usr/bin/env python
# -*- coding: utf-8 -*-

from libsplit import page2filename

def main():
    """docstring for split"""
    from codecs import open
    for i in range(1988, 1989):
        f = open('%s.markdown' %i, 'rb', 'utf-8')
        year = f.read().split('---')
        year.pop(0)
        for page in year:
            date, title, month, day, mind = page2filename(page)
            #import ipdb; ipdb.set_trace()
            #if len(title) == 0 or len(month) == 0 or len(day) == 0:
            print u'Yıl: %s Ay: %s\tGün: %s' %(i, month, day)
if __name__ == '__main__':
    main()
