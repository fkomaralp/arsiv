#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import gc ;gc.disable()
import sys
sys.path.insert(0, 'lib')
import codecs

from jinja2 import Environment
from jinja2.loaders import FileSystemLoader
POSTS = Environment(loader=FileSystemLoader('templates/'))

TEMPLATE = POSTS.get_template( 'mobile.html' )


from datetime import *
from dateutil.relativedelta import *
today = date.today()

import markdownapi as MD

   
def monthDays(yil,ay):
    buay =  date(yil, ay, 1)
    sonrakiay = buay + relativedelta(months=+1)
    cekiyor = abs( sonrakiay  - buay).days   # Bu ay kac cekiyor
    return cekiyor


def yazDosyaya(file, data, dir = None):
    data =  data.encode('utf-8').decode('utf-8')
    if dir is None:
        f = codecs.open('%s' %file , 'wb', 'utf-8')
        f.write(data)  
        return 0
    
    f = codecs.open('%s/%s' %(dir, file) , 'wb', 'utf-8')
    f.write(data)
    return 0
        
print 'Bismillah'
yil = 2014
#for ay in range(1,13):

def aylar(index):
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
    return aylar[index-1]
    
INDEX = \
'''
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <title>2014</title>
  <meta name="description" content="The HTML5 Herald">
      <style type="text/css">
body{

  top: 0px;
  margin: 0.5em 0.1em;
  padding: 0 auto;
  font-family : 'Georgia', 'Palatino', 'Palatino Linotype', Times, 'Times New Roman';
}
</style>
</head>
<body>
'''

FOOTER = '''
</body>
</html>
'''

 

for ay in range(1,13):
#for ay in range(2,3):
    for gun in range(1, monthDays(yil,ay) + 1):
#    for gun in range(1,2):
        tarih = date(yil,ay,gun)
        file = str(ay) + '-' + str(gun) 
        SOURCE = 'txt/%s.txt' % file
        RAW = codecs.open( SOURCE, 'rb' , 'utf-8').readlines()

        TITLE = RAW[:1][0].encode('utf-8').decode('utf-8')
        
        BODY = ''
        for line in RAW[1:]:
            BODY += line

        MARKDOWN = MD.render( BODY )
        
        DUMPHTML = TEMPLATE.render ( title = TITLE, metin = MARKDOWN )
        
        DUMPMARKDOWN = '## %s \n' %TITLE + MD.render( BODY )
        # print HTM.encode('utf-8')
        yazDosyaya(file = '%s.html' %file, data = DUMPHTML, dir = 'html')
        yazDosyaya(file = '%s.markdown' %file, data = DUMPMARKDOWN, dir = 'markdown')
        INDEX += '<a href="html/%s.html"><b>%s %s</b> | %s</a><br/>' %(file, gun, aylar(ay), TITLE)

INDEX += FOOTER
yazDosyaya( file = 'index.html', data = INDEX)
