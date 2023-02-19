import threading
from queue import Queue
from crawler import crawler
from domain import *
from  tstcrawler import *

PROJECT_NAME="samsung"
HOMEPAGE="https://www.samsung.com/in/"
DOMAIN_NAME=get_domain_name(HOMEPAGE)

QUEUE_FILE=PROJECT_NAME+"/queue.txt"
CRAWLED_FILE=PROJECT_NAME+"/crawled.txt"

NUMBER_OF_THREADS=8

queue=Queue()
crawler(PROJECT_NAME,HOMEPAGE,DOMAIN_NAME)

#suicide squad die when main is killed or dies :)
def create_workers():
	for _ in range(NUMBER_OF_THREADS):
		t=threading.Thread(target=work)
		t.daemon=True
		t.start()

def work():
	while True:
		url=queue.get()
		print("inside the wok func")
		#print("the url obtained:",url)
		crawler.crawlpage(threading.current_thread().name,url)
		queue.task_done()

def create_jobs():
	for link in fromfiletoset(QUEUE_FILE):
		queue.put(link)
	queue.join()
	crawl()

def crawl():
	queue_links=fromfiletoset(QUEUE_FILE)
	if (len(queue_links)>0):
		print(str(len(queue_links))+" links in the queue")
		create_jobs()

create_workers()
crawl()