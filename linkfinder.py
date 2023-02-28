from html.parser import HTMLParser
from urllib import parse

class LinkFinder(HTMLParser):
	def __init__(self,base_url,page_url):
		super().__init__()
		self.base_url=base_url
		self.page_url=page_url
		self.links=set()

	def handle_starttag(self,tag,attrs):
		print("i got called !")
		'''
		print(tag)
		if tag=="a":
			for (attribute,value) in attrs:
				if attribute=="href":
					print("found a link:",value)
					url=parse.urljoin(self.base_url,value)
					self.links.add(url)
		'''

	def appthelink(self,thelinktoappend):
		self.links.add(thelinktoappend)

	def pagelinks(self):
		return self.links

	def error(seld,message):
		pass

#import requests
#test=requests.get(url="https://en.wikipedia.org/wiki/Dog").text
#test=requests.get(url = 'https://google.com').text
#q=LinkFinder("https://www.youtube.com/","https://www.youtube.com/")
#q.feed("<!DOCTYPE html><html><head><title>Page Title</title></head><body><h1>This is a Heading</h1><a href='erukumo.com'></a><p>This is a paragraph.</p></body></html>")
#q.feed(test)

#q=LinkFinder("https://en.wikipedia.org/wiki/Dog","https://en.wikipedia.org/wiki/Dog")
#q.feed(test)