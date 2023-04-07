import os

flag=0

def create_project_dir(directory):
	if not os.path.exists(directory):
		print("Creating a new project directory "+directory)
		os.makedirs(directory)

def create_data_files(projectname,baseurl):
	queue=projectname+"/queue.txt"
	crawled=projectname+"/crawled.txt"
	print("writting base url to the queue file")
	if not os.path.isfile(queue):
		print("the base url0:",baseurl)
		write_file(queue,baseurl)
	if not os.path.isfile(crawled):
		write_file(crawled,"")

def write_file(path,data):
	f=open(path,"w")
	f.write(data)
	f.close()

def addtofile(path,data):
	print("writting ",data,"to file ",path)
	with open(path,"a",encoding="utf-8") as file:
		file.write(data+"\n")

def deletefilecontent(path):
	with open(path,"w"):
		pass

#read the to be crawled txt and add them to a set. set because to avoid data duplicacy
def fromfiletoset(filename):
	print("reading from file")
	results=set()
	with open(filename,"rt") as f:
		for line in f:
			print("line in file: ",line)
			try:
				results.add(line.replace("\n",""))
			except:
				return results
	print("theresults: ",results)
	return results

#read the set and add the links in set to a txt file
def fromsettofile(links,file):
	print("writting to file")
	'''
	if flag<10:
		deletefilecontent(file)
		for link in sorted(links):
			print("writing this to file:",link)
			addtofile(file,link)
		flag+=1
	else:
		print("flag passed not writting to file :)")
	'''
	deletefilecontent(file)
	for link in sorted(links):
		addtofile(file,link)

def createcontentfile(projectname):
	content=projectname+"/content.txt"
	#crawled=projectname+"/crawled.txt"
	print("writting content to the content file")
	if not os.path.isfile(content):
		#print("the base url0:",baseurl)
		write_file(content,"")


#create_project_dir("testing")
#create_data_files("testing","https://vtop.vit.ac.in/vtop/login")