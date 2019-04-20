import urllib.request

print('Beginning file download with urllib2...')

url = 'https://images.unsplash.com/photo-1493441883526-0ed85220dc0c?ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=60'  
urllib.request.urlretrieve(url, 'cat.jpg')