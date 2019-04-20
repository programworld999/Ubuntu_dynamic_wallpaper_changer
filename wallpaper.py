import os
import validators
import urllib.request as DFU


def downloadFile(url):
	print('Processing.........')
	DFU.urlretrieve(url, '/home/programworld999/Desktop/python/Python/wallpaper/.wallpaper.jpg')
	setwallpaper('.wallpaper.jpg')


def setwallpaper(image):
	try:
		os.system('cp /home/programworld999/Desktop/python/Python/wallpaper/.wallpaper.jpg /home/programworld999/Pictures/Wallpapers')
		os.system('clear')
		print('\033[1m \033[92m Wallpaper Change Successful! \033[0m')
	except:
		print('\033[1m \033Faild! \033[0m')

image = input('Enter Image URL: ')

url_cheak = validators.url(image)
if url_cheak == True:
	print('Online Image')
	downloadFile(image)
else:
	print('Local Image')
	os.system('cp '+image+' /home/programworld999/Desktop/python/Python/wallpaper/.wallpaper.jpg')
	setwallpaper('null')