import os
import urllib.request as DFU


def downloadFile(url):
	print('Processing.........')
	DFU.urlretrieve(url, '.wallpaper.jpg')
	setwallpaper()


def setwallpaper():
	try:
		os.system('cp .wallpaper.jpg /home/programworld999/Pictures/Wallpapers')
		os.system('clear')
		print('\033[1m \033[92m Wallpaper Change Successful! \033[0m')
	except:
		print('\033[1m \033Faild! \033[0m')

image = input('Enter Image URL: ')

downloadFile(image)
