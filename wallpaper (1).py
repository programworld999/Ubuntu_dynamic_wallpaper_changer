#!/usr/bin/env python
# coding: utf-8

# In[164]:


import os
import requests
from bs4 import BeautifulSoup
import urllib.request as DFU
import time


# In[165]:


def getScraped(url):
    data=requests.get(url)
    soup = BeautifulSoup(data.text, 'html.parser')
    return soup


# In[166]:


def getCatalogs(data):
    catalogs = data.find_all('ul', class_='filters__list')
    catalogs = catalogs[0]
    catalogs = catalogs.find_all('li')
    i=0
    for i in range(0, len(catalogs)):
        link=catalogs[i].find('a')['href']
        link="https://wallpaperscraft.com"+link
        catalogs[i]=link
    for i in range(0, len(catalogs)):
        name = catalogs[i].replace('https://wallpaperscraft.com/catalog/', '')
        link = catalogs[i]
        catalogs[i] = {'id': (i+1), 'name': name, 'link': link}
    return catalogs


# In[167]:


def totalImages(catalog):
    data = getScraped(catalog['link'])
    count=data.find_all('a', class_="pager__link")
    count = count[len(count)-1]['href']
    count = count.replace('/catalog/'+catalog['name']+'/page', '')
    count = int(count)*15
    return count


# In[168]:


def getWallpapersSrc(catalog):
    data = getScraped(catalog['link'])
    wallpapers=data.find_all('img', class_="wallpapers__image")
    for i in range(0, len(wallpapers)):
        src=wallpapers[i]['src']
        src=src.replace('300x168', '1280x720')
        wallpapers[i]=src
    return wallpapers


# In[169]:


def downloadWallpaper(url, name):
    print('Processing.........')
    DFU.urlretrieve(url, './wallpaper/.wallpaper_'+str(name)+'.jpg')


# In[170]:


def StartDynamicWallpaper():
    for i in range(0, 5):
        os.system('cp ./wallpaper/.wallpaper_'+str(i)+'.jpg ./wallpaper/.wallpaper/')
        os.system('mv ./wallpaper/.wallpaper/.wallpaper_'+str(i)+'.jpg ./wallpaper/.wallpaper/.wallpaper.jpg')
        os.system('cp ./wallpaper/.wallpaper/.wallpaper.jpg /home/sk/Pictures/Wallpapers')
        time.sleep(4)
    StartDynamicWallpaper()


# In[171]:


url = "https://wallpaperscraft.com/"
data = getScraped(url)
catalogs = getCatalogs(data)


# In[172]:


for i in range(0, len(catalogs)):
    print(str(catalogs[i]['id'])+".", catalogs[i]['name'])
print("Select Catalogs: ")
catalog = int(input())
catalog = catalogs[(catalog-1)]
catalog
# print("Available Images : ", totalImages(catalog), ". How Many Do You Want To Use: ")
# imagesUse = input()
wallpapers = getWallpapersSrc(catalog)
for i in range(10,len(wallpapers)):
    downloadWallpaper(wallpapers[i], (i-10))
StartDynamicWallpaper()


# In[ ]:




