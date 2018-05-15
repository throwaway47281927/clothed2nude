import re
import socks
import socket
import urllib2
from bs4 import BeautifulSoup

BASE_URL = "https://www5.zippyshare.com"
socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, "127.0.0.1", 9050)
socket.socket = socks.socksocket
html = urllib2.urlopen(BASE_URL + "/v/iep3IFuD/file.html").read()
match = re.search("getElementById\(\'dlbutton\'\)\.href = ([^;]*)", html)
js = match.group(1).replace("(", "str(")
url = BASE_URL + eval(js)
with open("./original.tar.gz", 'wb') as output:
    req = urllib2.Request(url)
    opener = urllib2.build_opener()
    bytes = opener.open(req).read()
    output.write(bytes)
