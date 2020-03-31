import os
# import validators
# import urllib.request as DFU
import requests
from bs4 import BeautifulSoup

# def downloadFile(url):
# 	print('Processing.........')
# 	DFU.urlretrieve(url, './wallpaper/.wallpaper.jpg')
# 	setwallpaper('.wallpaper.jpg')


# def setwallpaper(image):
# 	try:
# 		os.system('cp ./wallpaper/.wallpaper.jpg /home/programworld999/Pictures/Wallpapers')
# 		os.system('clear')
# 		print('\033[1m \033[92m Wallpaper Change Successful! \033[0m')
# 	except:
# 		print('\033[1m \033Faild! \033[0m')

# image = input('Enter Image URL: ')

# url_cheak = validators.url(image)
# if url_cheak == True:
# 	print('Online Image')
# 	downloadFile(image)
# else:
# 	print('Local Image')
# 	os.system('cp '+image+' /home/programworld999/Desktop/python/Python/wallpaper/.wallpaper.jpg')
# 	setwallpaper('null')


def getScraped(url):
	data=requests.get(url)
	soup = BeautifulSoup(data.text, 'html.parser')
	return soup



if __name__ == "__main__":
	url = "https://wallpaperscraft.com/"
	data = getScraped(url)
	catagorys = data.find_all('ul', attr={'class': 'filters__list'})
	# data = data.find('ul', attr={'class': 'JS-Filters'})
	
	print(catagorys[1])
