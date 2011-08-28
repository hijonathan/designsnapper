import pycurl
from BeautifulSoup import BeautifulSoup
import hashlib

def hash_content(content):
    soup = BeautifulSoup(content)
    content = soup.findAll(attrs={"id":"family-prod-macmini"})
    for x in content:
        hash = hashlib.sha224(x.renderContents())
        print hash.hexdigest()

c = pycurl.Curl()
c.setopt(c.URL, "http://store.apple.com/us")
c.setopt(c.WRITEFUNCTION, hash_content)
c.setopt(c.FOLLOWLOCATION,1)
c.perform()
