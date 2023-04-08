import threading
from queue import Queue
from crawler import crawler
from domain import *
from  tstcrawler import *

import tkinter as tk

NUMBER_OF_THREADS=8
queue=Queue()

class ScrollableText(tk.Frame):
    def __init__(self, master, text="", *args, **kwargs):
        tk.Frame.__init__(self, master, *args, **kwargs)
        self.canvas = tk.Canvas(self, width=500, height=500)
        self.scrollbar = tk.Scrollbar(self, orient="vertical", command=self.canvas.yview)
        self.scrollable_frame = tk.Frame(self.canvas)
        
        self.scrollable_frame.bind("<Configure>", lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))
        
        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        self.canvas.configure(yscrollcommand=self.scrollbar.set)
        
        self.scrollbar.pack(side="right", fill="y")
        self.canvas.pack(side="left", fill="both", expand=True)
        
        self.paragraph = tk.Label(self.scrollable_frame, text=text, wraplength=450)
        self.paragraph.pack(fill="both", padx=20, pady=10)

class InputLoader(tk.Frame):
    def __init__(self, master, *args, **kwargs):
        tk.Frame.__init__(self, master, *args, **kwargs)
        self.input_label = tk.Label(self, text="Enter your text here:")
        self.input_entry = tk.Entry(self, width=50)
        self.submit_button = tk.Button(self, text="Submit", command=self.load_paragraph)
        
        self.input_label.pack(pady=10)
        self.input_entry.pack(pady=10)
        self.submit_button.pack(pady=10)
    
    def load_paragraph(self):
        input_text = self.input_entry.get()
        self.input_entry.delete(0, tk.END)

        PROJECT_NAME=input_text
        HOMEPAGE=f"https://en.wikipedia.org/wiki/{PROJECT_NAME}"

        DOMAIN_NAME=get_domain_name(HOMEPAGE)

        global QUEUE_FILE,CRAWLED_FILE

        print("domain name:",DOMAIN_NAME)
        QUEUE_FILE=PROJECT_NAME+"/queue.txt"
        CRAWLED_FILE=PROJECT_NAME+"/crawled.txt"        

        #queue=Queue()
        global queue
        queue.put(HOMEPAGE)
        crawler(PROJECT_NAME,HOMEPAGE,DOMAIN_NAME,PROJECT_NAME)

        create_workers()
        crawl()

        print("reading from file")
        toprintresults=""
        thecontentfilepath=f"{PROJECT_NAME}/content.txt"
        with open(thecontentfilepath,"rt",encoding="utf8") as f:
        	for line in f:
        		try:
        			toprintresults+=line
        		except:
        			pass
        print("theresults: ",toprintresults)

        text_frame = ScrollableText(root, text=toprintresults)
        text_frame.pack(fill="both", expand=True)


'''
PROJECT_NAME="bottle"
HOMEPAGE=f"https://en.wikipedia.org/wiki/{PROJECT_NAME}"
#MAX=50

#PROJECT_NAME="SAMSUNG"
#HOMEPAGE="https://www.samsung.com/in/"
DOMAIN_NAME=get_domain_name(HOMEPAGE)

print("domain name:",DOMAIN_NAME)
QUEUE_FILE=PROJECT_NAME+"/queue.txt"
CRAWLED_FILE=PROJECT_NAME+"/crawled.txt"

NUMBER_OF_THREADS=8

queue=Queue()
queue.put(HOMEPAGE)
#createcontentfile(PROJECT_NAME)
crawler(PROJECT_NAME,HOMEPAGE,DOMAIN_NAME,PROJECT_NAME)
'''

#suicide squad die when main is killed or dies :)
def create_workers():
	global NUMBER_OF_THREADS
	for _ in range(NUMBER_OF_THREADS):
		t=threading.Thread(target=work)
		t.daemon=True
		t.start()

def work():
	global queue
	print("inside work")
	while True:
		print("test inside")
		url=queue.get()
		print("inside the wok func")
		#print("the url obtained:",url)
		crawler.crawlpage(threading.current_thread().name,url)
		queue.task_done()

def create_jobs():
	global queue,QUEUE_FILE
	for link in fromfiletoset(QUEUE_FILE):
		queue.put(link)
	queue.join()
	try:
		crawl()
	except:
		return

def crawl():
	global QUEUE_FILE
	queue_links=fromfiletoset(QUEUE_FILE)
	if (len(queue_links)>0):
		print(str(len(queue_links))+" links in the queue")
		try:
			create_jobs()
		except:
			return
	else:
		return

# create_workers()
# crawl()

print("asd")

root = tk.Tk()
root.title("WEB MINING J COMPONENT")

input_loader = InputLoader(root)
input_loader.pack(fill="both", expand=True)

root.mainloop()

print("terminated successfully ! :)")