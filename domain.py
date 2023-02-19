from urllib.parse import urlparse

def get_domain_name(url):
	print("here0")
	try:
		print("00")
		results=get_sub_domain_name(url).split(".")
		return results[-2]+"."+results[-1]
	except:
		print("01")
		return ""

def get_sub_domain_name(url):
	print("here1")
	try:
		print("10")
		return urlparse(url).netloc
	except:
		print("11")
		return ""

#print(get_domain_name("https://www.google.com/"))
#print(get_domain_name("https://www.youtube.com/"))