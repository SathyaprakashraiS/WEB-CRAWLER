from html.parser import HTMLParser
from urllib import parse

import multiprocessing
from bs4 import BeautifulSoup
from queue import Queue, Empty
from concurrent.futures import ThreadPoolExecutor
from urllib.parse import urljoin, urlparse
import requests

class Reader(HTMLParser):
	def __init__(self):
		pass
	def fres(url):
		try:
			res = requests.get(url, timeout=(3, 30))
			print(res)
			return res
		except requests.RequestException:
			return
	def parse_links(self, html):
		soup = BeautifulSoup(html, 'html.parser')
		Anchor_Tags = soup.find_all('a', href=True)
		for link in Anchor_Tags:
			url = link['href']
			if url.startswith('/'):
				print("in start with print")
				#url = urljoin(self.root_url, url)
				#if url not in self.scraped_pages:
				#	self.crawl_queue.put(url)
	def test(res):
		result = res.result()
		if result and result.status_code == 200:
			parse_links(result.text)
	def scrapcontent(self,html):
		print("html is",html)
		soup = BeautifulSoup(html, "html5lib")
		web_page_paragraph_contents = soup('p')
		text = ''
		for para in web_page_paragraph_contents:
			if not ('https:' in str(para.text)):
				text = text + str(para.text).strip()
		print(f'\n <---Text Present in The WebPage is --->\n', text, '\n')
		return
	def scraptext(url,word):
		#url = 'https://www.example.com'
		response = requests.get(url)
		html_content = response.content
		soup = BeautifulSoup(html_content, 'html.parser')
		#print(soup.get_text())
		thetext=soup.get_text()
		if word.lower() in thetext.lower():
			print("erukku")
		else:
			print("illa")
q=Reader
url="https://en.wikipedia.org/wiki/cat"
#theres=q.fres("https://en.wikipedia.org/wiki/cat")
#q.test(theres)
q.scraptext(url,"cAt")
