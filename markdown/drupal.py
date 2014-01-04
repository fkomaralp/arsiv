#!/usr/bin/env python
# -*- coding: utf-8 -*-

from libsplit import page2filename
import codecs

from os import listdir
from os.path import isfile, join

from drupal.services import *
from drupal.config import config
from drupal.interface import node

def main():
    "docstring for split"""
    yillar = [ y for y in range(1988,1998) if y != 1993 ]
    #for yil in [1989]:
    for yil in yillar:
        mypath = str(yil)
        files = [ f for f in listdir(mypath) if isfile(join(mypath,f)) ]
        for file in files:
            ay = file.split('.')[0].split('-')[0]
            gun = file.split('.')[0].split('-')[1]
            f = codecs.open('%s/%s' %(yil,file), 'r', 'utf-8')
            dump = f.readlines()
            body = u''''''
            for row in dump[1:]:
                body += row
            title = dump[0].strip('#').strip()
            #print yil,ay,gun,title
            new_node = node(year = yil, month = ay, day =gun,
                    title = title,
                    body = body
                    )

            if title == '':
                print '%s/%s-%s.markdown' %(yil, ay,gun)
            #dp = DrupalServices(config)
            
            #dp.call('node.create', new_node)

if __name__ == '__main__':
    main()
