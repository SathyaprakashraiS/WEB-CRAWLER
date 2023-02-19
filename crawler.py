from urllib.request import urlopen
from linkfinder import LinkFinder
from tstcrawler import *

class crawler:
	projectname=""
	baseurl=""
	domainname=""
	queuefile=""
	crawledfile=""
	queue=set()
	crawled=set()

	def __init__(self,projectname,baseurl,domainname):
		crawler.projectname=projectname
		crawler.baseurl=baseurl
		crawler.domainname=domainname
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
		if page_url not in crawler.crawled:
			print(thread_name+" crawling "+page_url)
			print("Queue "+str(len(crawler.queue)))
			print("Crawled "+str(len(crawler.crawled)))
			crawler.appendlinkstoqueue(crawler.gatherlinks(page_url))
			crawler.queue.remove(page_url)
			crawler.crawled.add(page_url)
			crawler.updatefiles()

	@staticmethod
	def gatherlinks(page_url):
		html_string=""
		try:
			response=urlopen(page_url)
			print("response:",response)
			if response.getheader("Content Type")=="text/html":
				html_bytes=response.read()
				html_string=html_bytes.decode("utf-8")
			finder=LinkFinder(crawler.baseurl,page_url)
			finder.feed(html_string)
		except:
			print("Error: cannot crawl page")
			return set()
		return finder.pagelinks()

	@staticmethod
	def appendlinkstoqueue(links):
		for url in links:
			if url in crawler.queue:
				continue
			if url in crawler.crawled:
				continue
			#add to stop it from crawling non domain pages
			if crawler.domainname not in url:
				continue

	@staticmethod
	def updatefiles():
		fromsettofile(crawler.queue,crawler.queuefile)
		fromsettofile(crawler.crawled,crawler.crawledfile)

#print("qwe")