#!/usr/bin/env python
# -*- coding: utf-8 -*-
##
#  @file Ninjafy.py
#  @brief Brief
#
import gc
gc.disable()


from os import mkdir, chdir, getcwd, system
from os.path import join
import codecs
import time as tm
import locale
locale.setlocale(locale.LC_ALL,'')
#locale.setlocale(locale.LC_ALL,'TR_TR')
locale.setlocale(locale.LC_ALL, 'tr_TR.utf-8')
print locale.getlocale()


print '-' * 33
import os
print os.getcwd()
from datetime import *
from dateutil.relativedelta import *
import re
from jinja2 import Environment
from jinja2.loaders import FileSystemLoader
env = Environment(loader=FileSystemLoader('templates/'))
# SIMPLE = env.get_template('simple.md')
SIMPLE = env.get_template('tiny.md')

#print SIMPLE.render()

def okuDosyadan(filename):
    inputFolder = 'txt/'
    filename = inputFolder + filename
    str = ''''''
    baslik = ''''''
    try:
        f = codecs.open(filename,'rb', 'utf-8')
    except:
        pass
    i = 0
    for r in f.readlines():
        i += 1
        if i == 1:
            baslik = r.encode('utf-8')
            continue
        str += r.encode('utf-8')
    f.close()
    return  (baslik, str)

def yazDosyaya(filename, metin):
    outputFolder = '_debug/' + str(yil) + '/'
    fullOutput = outputFolder + filename + '.markdown'

    metin =  metin.encode('utf-8').decode('utf-8')
    f = codecs.open(fullOutput, 'wb', 'utf-8')
    f.write(metin)
    return 0


def cleanQuotes(str):
    str = str.replace('\"','')
    return str

def aylar():
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
    return aylar


def htmlEntityEncode(str):
    return str.encode('ascii', 'xmlcharrefreplace').encode('utf-8')

def temizle(str):
    str = str.rstrip('\r\n')
    str = str.lstrip('\r\n')
    return str

def trAy(tarih):
    str = tarih.strftime('%B')
    return str.decode('cp1254').encode('utf-8').decode('utf-8')

def trTarihFilename(tarih):
    str = tarih.strftime('%Y-%m-%d')
    return str.decode('cp1254').encode('utf-8').decode('utf-8')

def trTarihFolder(tarih):
    str = tarih.strftime('%Y-%m')
    return str.decode('cp1254').encode('utf-8').decode('utf-8')

def trTarih(tarih, gunIsmi=True):

    # dt = date(yil,ay,gun)
    if gunIsmi:
        str = tarih.strftime('X%d %B %A').replace('X0', 'X').replace('X','')
    else:
        str = tarih.strftime('X%d %B').replace('X0', 'X').replace('X','')
    return str # Ubuntu
    return str.decode('cp1254').encode('utf-8') # Windows

def monthDays(yil,ay):
    buay =  date(yil, ay, 1)
    sonrakiay = buay + relativedelta(months=+1)
    cekiyor = abs( sonrakiay  - buay).days   # Bu ay kac cekiyor
    return cekiyor

def translit(str):
    from unidecode import unidecode
    str = unidecode(str)
    str = str.strip()
    str = str.replace(' ','-')
    str = str.replace('!','')
    str = str.replace('<','')
    str = str.replace('*','')
    str = str.replace('/','-')
    str = str.replace(';','-')
    str = str.replace('>','')
    str = str.replace('\'','')
    str = str.replace('.','')
    str = str.replace(')','')
    str = str.replace('(','')
    str = str.replace('?','')
    str = str.replace(',','')
    str = str.replace(':','')
    str = str.replace('--','-')
    str = str.replace('\"','')
    str = str.lower()
    str = str.replace('allah','Allah')
    str = str.replace('peygamber','Peygamber')
    str = str.replace('habib','Habib')
    str = str.replace('kuran','Kuran')
    str = str.replace('mahmud','Mahmud')
    str = str.replace('sami','Sami')
    str = str.replace('ramazanoglu','Ramazanoglu')
    str = str.replace('nebi','Nebi')
    return str.encode('utf-8')


if __name__ == '__main__':
    print 'Bismillah'

    yil = 2014

    for ay in range(1,13):
#    for ay in range(1,2):
        for gun in range(1, monthDays(yil,ay) + 1):
#         for gun in range(1,2):
            tarih = date(yil,ay,gun)
            fileNoExt = str(ay) + '-' + str(gun)
            file =  fileNoExt +  '.txt'
            jtarih = trTarih(tarih).decode('utf-8')

            title, metin = okuDosyadan(file)
            metin = metin.decode('utf-8')
            title = cleanQuotes(temizle(title.decode('utf-8')))
            title_html = htmlEntityEncode(title)
            HTM = SIMPLE.render(title_html = title_html , title=title, metin=metin,
                tarih=jtarih)

            # print HTM.encode('utf-8')
            yazDosyaya(fileNoExt, HTM)


