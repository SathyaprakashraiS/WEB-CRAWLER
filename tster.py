from urllib.request import urlopen,Request
from linkfinder import *
import requests

def gatherlinks(page_url):
	print("in gsther links")
	html_string=""

	#dir run
	#response=requests.get(url = 'https://google.com').text
	response=requests.get(url=page_url).text
	finder=LinkFinder("https://www.samsung.com/in/",page_url)
	finder.feed(response)
	return finder.pagelinks()

	# print("in gsther links")
	# html_string=""
	# try:
	# 	response=urlopen(page_url)
	# 	print("response:",response)
	# 	if response.getheader("Content Type")=="text/html":
	# 		html_bytes=response.read()
	# 		html_string=html_bytes.decode("utf-8")
	# 	finder=LinkFinder(crawler.baseurl,page_url)
	# 	finder.feed(html_string)
	# except:
	# 	print("Error: cannot crawl page")
	# 	return set()
	# return finder.pagelinks()

q=set()
#q=gatherlinks("https://www.samsung.com/in/")
q=gatherlinks("https://www.samsung.com/in/")
print("the q",q)
#response=urlopen("https://www.samsung.com/in/")