import os

def create_project_dir(directory):
	if not os.path.exists(directory):
		print("Creating a new project directory "+directory)
		os.makedirs(directory)

def create_data_files(projectname,baseurl):
	queue=projectname+"/queue.txt"
	crawled=projectname+"/crawled.txt"
	if not os.path.isfile(queue):
		write_file(queue,baseurl)
	if not os.path.isfile(crawled):
		write_file(crawled,"")

def write_file(path,data):
	f=open(path,"w")
	f.write(data)
	f.close()

def addtofile(path,data):
	with open(path,"a") as file:
		file.write(data+"\n")

def deletefilecontent(path):
	with open(path,"w"):
		pass

#read the to be crawled txt and add them to a set. set because to avoid data duplicacy
def fromfiletoset(filename):
	results=set()
	with open(filename,"rt") as f:
		for line in f:
			results.add(line.replace("\n",""))
	return results

#read the set and add the links in set to a txt file
def fromsettofile(links,file):
	deletefilecontent(file)
	for link in sorted(links):
		addtofile(file,link)



#create_project_dir("testing")
#create_data_files("testing","https://vtop.vit.ac.in/vtop/login")