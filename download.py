import socks
import socket
import urllib2
from bs4 import BeautifulSoup

socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, "127.0.0.1", 9050)
socket.socket = socks.socksocket
html = urllib2.urlopen("https://cdn-02.anonfile.com/47pds4e3be/").read()
soup = BeautifulSoup(html, 'html.parser')
link = soup.find_all('a', {'id': 'download-url'})
url = link[0].attrs.get('href')
with open("./dataset.tar.gz", 'wb') as output:
    req = urllib2.Request(url)
    opener = urllib2.build_opener()
    output.write(opener.open(req).read())

print link