import requests
import re
import urllib
import time
from bs4 import BeautifulSoup
url=''
downloadPath='/Users///'
threadName='my_thread'
#Give the range of pages to download
for i in range(1,334):
    currenturl=url+`i`
    time.sleep(2)
    prefix=threadName+`i`+'-'
    html = requests.get(currenturl).text
    soup = BeautifulSoup(html, 'html.parser')
    soup2=soup.findAll("div", {"id" : re.compile('post_message.*')})
    print('For URL ' + currenturl)
    for posts in soup2: 
            for link in posts.find_all('img'):
                 try:  
                	  
                    if re.search('imagehostname', link.get('src')):
                      
                      filename=link.get('src').split("/")
                      ext=filename[len(filename)-1].split(".")
                      if len(ext)==1:
                         if(ext[1]==gif):
                            continue
		      
                      fileabsolute=filename[len(filename)-1]
                      if len(filename) < 4:
                          continue
                      perURL=''
                      for x in range(len(filename)):
                         if x ==0:
                            perURL=perURL+filename[x]+'//'
                         elif x==1:
                            perURL=perURL+filename[x]
                         elif x==2:
                            perURL=perURL+filename[x]
                         elif x ==3:
                            perURL=perURL+'/i'
                         else:
                            perURL=perURL+'/'+filename[x]
                      print 'image:    ',perURL
                      f = open(downloadPath+prefix+fileabsolute, 'wb')
                      f.write(requests.get(perURL).content)
                      f.close()
                      time.sleep(2)
                 except Exception:
                   pass
