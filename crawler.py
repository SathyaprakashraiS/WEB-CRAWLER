from urllib.request import urlopen
from linkfinder import LinkFinder
from tstcrawler import *
import requests
from bs4 import BeautifulSoup

from reader import Reader

#import multiprocessing
#from bs4 import BeautifulSoup
from queue import Queue, Empty
#from concurrent.futures import ThreadPoolExecutor
from urllib.parse import urljoin, urlparse
#import requests

import re

topic="cat"
#flag=0

class crawler:
	projectname=""
	baseurl=""
	domainname=""
	queuefile=""
	crawledfile=""
	topic=""
	seed_url =""
	root_url =""
	flag=0
       
	queue=set()
	crawled=set()

	summary=""

	def __init__(self,projectname,baseurl,domainname,topic):
		crawler.projectname=projectname
		crawler.baseurl=baseurl
		crawler.domainname=domainname
		crawler.topic="cat"
		crawler.queuefile=crawler.projectname+"/queue.txt"
		crawler.crawledfile=crawler.projectname+"/crawled.txt"
		
		crawler.flag=0

		crawler.seed_url = baseurl
		crawler.root_url = '{}://{}'.format(urlparse(self.seed_url).scheme,urlparse(self.seed_url).netloc)

		crawler.summary=""

		self.boot()
		self.crawlpage("first crawler",crawler.baseurl)

	@staticmethod
	def boot():
		create_project_dir(crawler.projectname)
		create_data_files(crawler.projectname,crawler.baseurl)
		crawler.queue=fromfiletoset(crawler.queuefile)
		crawler.crawled=fromfiletoset(crawler.crawledfile)

	@staticmethod
	def crawlpage(thread_name,page_url):
		print("in tthis function")
		print("crawled:",crawler.crawled)
		if page_url not in crawler.crawled:
			if(len(crawler.crawled)<=10):
				print("page url not in crawled file")
				print(thread_name+" crawling "+page_url)
				print("Queue "+str(len(crawler.queue)))
				print("Crawled "+str(len(crawler.crawled)))
				#crawler.gatherlinks(page_url)
				crawler.appendlinkstoqueue(crawler.gatherlinks(page_url))
				try:
					crawler.queue.remove(page_url)
				except:
					pass
				#for i in range(100):
				print("got returned")
				crawler.crawled.add(page_url)
				crawler.updatefiles()
			else:
				try:
					crawler.queue.remove(page_url)
				except:
					pass
				#for i in range(100):
				print("crawled many in else")
				crawler.crawled.add(page_url)
				crawler.updatefiles()				

	@staticmethod
	def gatherlinks(page_url):
		wikipedia_pattern = r'^https?://([a-z]+\.)?wikipedia\.org/wiki/'
		'''
		testqueue=set()
		#soup = BeautifulSoup(page_url, 'html.parser')
		soup=BeautifulSoup(urlopen(page_url))
		soup=BeautifulSoup(soup,'html.parser')
		print("soup is ",soup)
		#urlopen(URL)
		Anchor_Tags = soup.find_all('a', href=True)
		for link in Anchor_Tags:
			url = link['href']
			if url.startswith('/') or url.startswith(crawler.root_url):
				url = urljoin(crawler.root_url, url)
				if url not in crawler.crawled:
					testqueue.add(url)
		finder=LinkFinder(crawler.baseurl,page_url)
		return finder.pagelinks()
		'''

		print("in gather links")
		print("the page to be crawled is: ",page_url)
		#global flag
		#this code is to find page relevance to the given topic
		html_string=""
		summary=""
		finder=LinkFinder(crawler.baseurl,page_url)
		try:
			response=requests.get(page_url)
			soup=BeautifulSoup(response.content, 'html.parser')
			try:
				print("in try block")
				q=Reader
				#theres=q.fres("https://en.wikipedia.org/wiki/cat")
				#q.test(theres)
				text,score=q.scraptext(page_url,"cat")
				#print("the text is ",text)
				print("the score is ",score)
				if(score>0.7):
					print("text length is",len(text))
					summary=q.summarisecontent(text)
					print("summary length is",len(summary))
					crawler.writesumcontenttofile(crawler.projectname,summary)
					q=[]
					q=soup.find_all('a')
					print("q length is",len(q))
					# for links in q:
					# 	print(links)
					for links in soup.find_all('a'):
						href=links.get('href')
						print("link is ",links)
						print("href is ",href)
						if(re.match(wikipedia_pattern, href)):
							print("the link adding to queue is ",href)
							crawler.appendsinglelinktoqueue(href)
						#if href.startswith('http'):
						#	print("the link adding to queue is ",href)
						#	crawler.appendsinglelinktoqueue(href)
						else:
							print("in else")
					return finder.pagelinks()
					'''
						if(crawler.flag<100):
							crawler.flag+=1
							href=link.get('href')
							if href.startswith('http'):
								try:
								print("ulla eruken")
								q=Reader
								#theres=q.fres("https://en.wikipedia.org/wiki/cat")
								#q.test(theres)
								text,score=q.scraptext(link,"cAt")
								if(score>0):
									print("text length is",len(text))
									summary=q.summarisecontent(text)
									print("summary length is",len(summary))
								else:
									pass
								except:
									print("thorathitan")
						else:
							return finder.pagelinks()
						'''
				else:
					print("page irrelevent")
					print("page score is ",score)
					return set()
			except:
				return set()
				'''
			q=[]
			q=soup.find_all('a')
			#print("toital links in page:",soup.find_all('a'))
			for link in soup.find_all('a'):
				if(crawler.flag<100):
					crawler.flag+=1
					##print("running",flag)
					href=link.get('href')
					print("ulla poga poren")
					##print("the link",href)
					try:
						if href.startswith('http'):
							try:
								print("ulla eruken")
								q=Reader
								#theres=q.fres("https://en.wikipedia.org/wiki/cat")
								#q.test(theres)
								text,score=q.scraptext(link,"cAt")
								if(score>0):
									print("text length is",len(text))
									summary=q.summarisecontent(text)
									print("summary length is",len(summary))
								else:
									pass
								
							except:
								print("thorathitan")
								##print("keyword mismatch topic aint relevant!")
								##rint("irrelevant link ",href)
								pass
					except:
						return finder.pagelinks()
				else:
					return finder.pagelinks()

'''

		except:
			print("Error: cannot crawl page")
			return set()
		return finder.pagelinks()

	@staticmethod
	def appendlinkstoqueue(links):
		print("in append links to queue")
		for url in links:
			#print("url is :",url)
			if url in crawler.queue:
				continue
			elif url in crawler.crawled:
				continue
			#add to stop it from crawling non domain pages
			#elif crawler.domainname not in url:
			#	continue
			else:
				crawler.queue.add(url)

	@staticmethod
	def appendsinglelinktoqueue(thelink):
		print("trying to append a single link")
		print("got this link: ",thelink)
		if thelink in crawler.queue:
			print("thelink in queue")
			pass
		elif thelink in crawler.crawled:
			print("the link in crawled list")
			pass
		#elif crawler.domainname not in url:
		#	print("domain name missing skipping url: ",thelink)
			pass
		else:
			print("added to queue")
		crawler.queue.add(thelink)
		print("added the link to queue")
		print("")

	@staticmethod
	def updatefiles():
		print("nan inga eruken :)")
		fromsettofile(crawler.queue,crawler.queuefile)
		fromsettofile(crawler.crawled,crawler.crawledfile)
		#fromsummarytofile(crawler.summary)

	@staticmethod
	def writesumcontenttofile(projectname,content):
		print("elutha poren in file")
		fromsummarytofile(projectname,content)

#print("qwe")