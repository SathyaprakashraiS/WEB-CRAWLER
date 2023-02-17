from html.parser import HTMLParser
from urllib import parse

class LinkFinder(HTMLParser):
	def __init__(self,base_url,page_url):
		super().__init__()
		self.base_url=base_url
		self.page_url=page_url
		self.links=set()

	def handle_starttag(self,tag,attrs):
		print(tag)
		if tag=="a":
			for (attribute,value) in attrs:
				if attribute=="href":
					url=parse.urljoin(self.base_url,value)
					self.links.add(url)

	def pagelinks(self):
		return self.links

	def error(seld,message):
		pass

#q=LinkFinder()
#q.feed("<!DOCTYPE html><html><head><title>Page Title</title></head><body><h1>This is a Heading</h1><p>This is a paragraph.</p></body></html>")