import bs4 as bs
import urllib.request

#with open('sites.txt', 'r') as f:
#    sites = []
#    for line in f:
#        sites.append(line.strip('\n'))

wikipedia = 'https://en.wikipedia.org'

site = 'https://en.wikipedia.org/wiki/Justin-Siena_High_School'
outfile = 'relatedto_js.txt'
sauce = urllib.request.urlopen(site).read()

soup = bs.BeautifulSoup(sauce, 'lxml')
bodyContent = soup.find(id="bodyContent")
output = open(outfile, 'w')
unique_a_tags = list(set(bodyContent.find_all('a')))

def getLinks():
    for link in unique_a_tags:
        if link.get('href'):
            new_url = link.get('href')
            if new_url[0:6] == '/wiki/': 
                try:
                    new_soup = bs.BeautifulSoup(urllib.request.urlopen(wikipedia + new_url).read(), 'lxml')
                except urllib.error.HTTPError:
                    pass
                output.write(new_soup.title.text + '\n')
                print(new_soup.title.text)
getLinks()
output.close()
