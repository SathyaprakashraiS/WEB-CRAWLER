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
		self.crawlpage("first crawler",crawler.base_url)

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
	


print("qwe")