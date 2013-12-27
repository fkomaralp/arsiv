# -*- coding: utf-8 -*-
import gc
gc.disable()

import Queue
import threading
queue = Queue.Queue()
from os import mkdir, chdir, getcwd, system
from os.path import join

import time as tm
from datetime import *
from dateutil.relativedelta import *

import time as tm
import locale
# locale.setlocale(locale.LC_ALL,'')
locale.setlocale(locale.LC_ALL,'Turkish_Turkey.1254')
print locale.getlocale()

import re


class tofile(threading.Thread):
    def __init__(self, queue):
        threading.Thread.__init__(self)
        self.queue = queue

    def run(self):
        now = datetime.now()
        while True:
            #grabs command from queue
            command = self.queue.get()
            print "%s | %s\n" % (self.getName(),command)
            system(command)

            #signals to queue job is done
            self.queue.task_done()

# -------------------------------------------------

def utf2html(str):
    return str.encode('ascii', 'xmlcharrefreplace').encode('utf-8')

def trTarih2(tarih):
    str = tarih.strftime('%Y-%m-%d')
    return str.decode('cp1254').encode('utf-8')

def trTarih(tarih, gunIsmi=True):

    # dt = date(yil,ay,gun)
    if gunIsmi:
        str = tarih.strftime('X%d %B %A').replace('X0', 'X').replace('X','')
    else:
        str = tarih.strftime('X%d %B').replace('X0', 'X').replace('X','')
    return str.decode('cp1254').encode('utf-8')

def monthDays(yil,ay):
    buay =  date(yil, ay, 1)
    sonrakiay = buay + relativedelta(months=+1)
    cekiyor = abs( sonrakiay  - buay).days   # Bu ay kac cekiyor
    return cekiyor

def dayOfYear(yil,ay,gun):
    dt = date(yil, ay, gun)
    return int(dt.strftime("%j"))

def removeBom(file):
    import os, sys, codecs
    BUFSIZE = 4096
    BOMLEN = len(codecs.BOM_UTF8)

    with open(file, "r+b") as fp:
        chunk = fp.read(BUFSIZE)
        if chunk.startswith(codecs.BOM_UTF8):
            i = 0
            chunk = chunk[BOMLEN:]
            while chunk:
                fp.seek(i)
                fp.write(chunk)
                i += len(chunk)
                fp.seek(BOMLEN, os.SEEK_CUR)
                chunk = fp.read(BUFSIZE)
            fp.seek(-BOMLEN, os.SEEK_CUR)
            fp.truncate()
    return 0

def trAylar():
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

def islecler():
    # commands = [] # Thread Queue Commands
    # command =  'pdf2txt.py -o %s -p%s %s' %(fullfile,page,pdf)
    # commands.append(command)
    #spawn a pool of threads, and pass them queue instance
    # start = tm.time()
    # for i in range(30):
        # t = tofile(queue)
        # t.setDaemon(True)
        # t.start()

    # #populate queue with data
    # for cmd in commands:
        # queue.put(cmd)

    # #wait on the queue until everything has been processed
    # queue.join()
    # print "Elapsed Time: %5f" % float((tm.time() - start))
    pass

def tests():
    yil = 2012
    ay =  2
    gun = 29

    myDate = date(2013,2,28)
    print 'Hello World'
    print monthDays(2013,12)
    print dayOfYear(2012,12,31)
    print trTarih(date(1988,1,1))
    str = u'''
    Ahmed Şeref Güneysu

    asdasd adsd
    '''
    print baslikTemizle(str)
    print utf2html(u'Şeref')

def temizle(str):
    str = str.strip('\r\n')
    return str

def yaziCikart(yil, ay, gun):
    import codecs
    f = codecs.open('txt/'+str(yil)+'.txt','rb', encoding='utf-8')

    dti = date(yil,ay,gun)
    dtf = dti + relativedelta(days=+1)

    stri = trTarih(dti)
    strf = trTarih(dtf)

    arkayuz = ''
    for r in f.readlines():
        arkayuz += r.encode('utf-8')
    # (1 Ocak Cuma)(.*)(?:2 Ocak Perşembe)
    """
    Match0 1 Ocak Cuma
    Match1 Metin
    """

    pat = '(?:%s)(.*)(?:%s)'  %(stri,strf)
    p = re.compile(pat, re.DOTALL+re.UNICODE)
    m = p.search(arkayuz)
    try:
        yazi =  m.groups(0)[0]
    except: # Bulamadi
        yazi =''
    f.close()
    return temizle(yazi.decode('utf-8'))

def dumptofile(tarih, metin):
    folder = tarih.strftime('%Y-%m/')
    try:
        mkdir( 'output/'+ folder )
    except:
        pass
    filename = 'output/' + folder + trTarih2(tarih) + '.txt'

    import codecs
    f = codecs.open(filename, 'wb', encoding='utf-8')

    f.write(metin)
    f.close()
    return 0

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
    # for yil in [1988]:
    # for yil in range(1988,1993)+range(1994,1998):
    for yil in range(1994,1998):
        for ay in range(1,13):
            for gun in range(1,monthDays(yil, ay)+1):
            # for gun in range(1,10):
                metin = yaziCikart(yil=yil, ay=ay, gun=gun)
                tarih = date(yil,ay,gun)
                dumptofile(tarih, metin)
