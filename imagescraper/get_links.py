import bs4 as bs
import urllib.request # Python 3

def get_urls(src, tag, link_type):
    array = []
    sauce = urllib.request.urlopen(src).read()
    soup = bs.BeautifulSoup(sauce, 'lxml')
    for link in soup.find_all(tag): 
        if link.get(link_type):
            new_url = link.get(link_type)
            if new_url[:4] == 'http':
                array.append(new_url)
    return array
