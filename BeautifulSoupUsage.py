from bs4 import BeautifulSoup as bs
from bs4 import SoupStrainer as soupstr
from PIL import Image
import io
import requests as rq
f=open('kai', 'w')
WebSource=rq.get("https://pixabay.com/en/photos/grill/?cat=food&image_type=photo")
WebSource2=rq.get("https://pixabay.com/en/photos/delicious%20baked%20pizza/?cat=food&image_type=photo&order=popular")
#WebSource.text @to get the source code of the page
cleanfst=bs(WebSource.text, 'lxml', parse_only=soupstr('img')) #to clean the source code and left behind img tag
cleanfst2=bs(WebSource2.text, 'lxml', parse_only=soupstr('img'))
cleanlist=cleanfst.find_all('img') #to create a list of image type source code
cleanlist2=cleanfst2.find_all('img')
Linklist=[]
for i in cleanlist:
    if i['src'] not in ["/static/img/blank.gif", '/static/img/facebook.svg','/static/img/instagram.svg','/static/img/twitter.svg']:
        Linklist+=[i['src']]
for j in cleanlist2:
    if j['src'] not in ["/static/img/blank.gif", '/static/img/facebook.svg','/static/img/instagram.svg','/static/img/twitter.svg','https://cdn.pixabay.com/photo/2018/01/14/20/49/dough-3082589__340.jpg','https://cdn.pixabay.com/photo/2018/03/07/18/42/menu-3206749__340.jpg','https://cdn.pixabay.com/photo/2018/03/07/18/42/menu-3206748__340.jpg']:
            Linklist+=[j['src']]
f.writelines(Linklist)