from urllib.request import urlopen
from linkfinder import LinkFinder
from tstcrawler import *
import requests
from bs4 import BeautifulSoup

topic="dog"
flag=0

class crawler:
	projectname=""
	baseurl=""
	domainname=""
	queuefile=""
	crawledfile=""
	topic=""
	queue=set()
	crawled=set()

	def __init__(self,projectname,baseurl,domainname,topic):
		crawler.projectname=projectname
		crawler.baseurl=baseurl
		crawler.domainname=domainname
		crawler.topic=topic
		crawler.queuefile=crawler.projectname+"/queue.txt"
		crawler.crawledfile=crawler.projectname+"/crawled.txt"
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
			print("page url not in crawled file")
			print(thread_name+" crawling "+page_url)
			print("Queue "+str(len(crawler.queue)))
			print("Crawled "+str(len(crawler.crawled)))
			crawler.appendlinkstoqueue(crawler.gatherlinks(page_url))
			crawler.queue.remove(page_url)
			crawler.crawled.add(page_url)
			crawler.updatefiles()

	@staticmethod
	def gatherlinks(page_url):
		print("in gather links")
		print("the page to be crawled is: ",page_url)
		flag=0
		#this code is to find page relevance to the given topic
		html_string=""
		finder=LinkFinder(crawler.baseurl,page_url)
		try:
			response=requests.get(page_url)
			soup=BeautifulSoup(response.content, 'html.parser')
			q=[]
			q=soup.find_all('a')
			#print("toital links in page:",soup.find_all('a'))
			for link in soup.find_all('a'):
				if(flag<100):
					flag+=1
					print("running",flag)
					href=link.get('href')
					print("the link",href)
					try:
						if href.startswith('http'):
							try:
								print("over here")
								linked_page = requests.get(href)
								linked_soup = BeautifulSoup(linked_page.content, 'html.parser')
								if crawler.topic in linked_soup.get_text():
									print("relevant")
									#finder.appthelink(href)
									crawler.appendsinglelinktoqueue(href)
									#crawler.queue.remove(href)
									#crawler.crawled.add(href)
									#crawler.updatefiles()
									print("relevant ",href)
							except:
								print("keyword mismatch topic aint relevant!")
								print("irrelevant link ",href)
					except:
						pass
				else:
					pass   
			#testing the code not sure
			# href=page_url.get('href')
			# print("the href:",href)
			# try:
			# 	if href.startswith('https'):
			# 		try:
			# 			linked_page=requests.get(href)
			# 			linked_soup=BeautifulSoup(linked_page.content, 'html.parser')
			# 			# Check if linked page contains relevant content
			# 			if topic in linked_soup.get_text():
			# 				print("this contains the topic",href)
			# 				response=requests.get(url=page_url).text
			# 				finder=LinkFinder(crawler.baseurl,page_url)
			# 				print("the response:",response)
			# 				finder.feed(response)  
			# 		except:
			# 			print("not in link")
			# except:
			# 	print("Error: cannot crawl page")
			# 	return set()    

			#this ocde works for the visualising part because its used to find pages conected and not relevance
			''' 
			response=requests.get(url=page_url).text
			finder=LinkFinder(crawler.baseurl,page_url)
			finder.feed(response)
			'''

			# response=urlopen(page_url)
			# print("response:",response)
			# if response.getheader("Content Type")=="text/html":
			# 	html_bytes=response.read()
			# 	html_string=html_bytes.decode("utf-8")
			# finder=LinkFinder(crawler.baseurl,page_url)
			# finder.feed(html_string)
		except:
			print("Error: cannot crawl page 0")
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

#print("qwe")