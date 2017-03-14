import os
import sys
import urllib.request # Python 3
import get_links

#FIXME: doesn't work for relative links

webpage = sys.argv[1]

split_on_slashes = sys.argv[1].split('/')
address = split_on_slashes[2].split('.')
address.pop()
folder = ""

for a in address:
    folder += a 
    folder += '.'
folder = folder[:-1]
folder += '/'
path = 'images_scraped/' + folder
if not os.path.exists(path):
    os.makedirs(path)

for url in get_links.get_urls(webpage, 'img', 'src'):
    urllib.request.urlretrieve(url, path + url.split('/')[-1])
