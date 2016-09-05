import httplib
import urllib

# latest ganwiki url
# http://stackoverflow.com/questions/22676/how-do-i-download-a-file-over-http-using-python
url = "https://dumps.wikimedia.org/ganwiki/latest/ganwiki-latest-pages-articles.xml.bz2"
urllib.urlretrieve(url, "ganwiki-latest-pages-articles.xml.bz2")

