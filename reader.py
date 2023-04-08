from html.parser import HTMLParser
from urllib import parse

import multiprocessing
from bs4 import BeautifulSoup
from queue import Queue, Empty
from concurrent.futures import ThreadPoolExecutor
from urllib.parse import urljoin, urlparse
import requests


import gensim
from gensim.summarization import summarize

import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.stem import PorterStemmer

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
		'''
		#url = 'https://www.example.com'
		response = requests.get(url)
		html_content = response.content
		soup = BeautifulSoup(html_content, 'html.parser')
		#print(soup.get_text())
		thetext=soup.get_text()
		return thetext
		if word.lower() in thetext.lower():
			print(thetext)
			print("erukku")
		else:
			print("illa")
		'''
		response = requests.get(url)
		soup = BeautifulSoup(response.content, "html.parser")
		main_content = soup.find("div", {"id": "mw-content-text"})
		paragraphs = main_content.find_all("p")
		text = ""
		for p in paragraphs:
			text += p.get_text()
		return text
	def summarisecontent(content):
		summary = summarize(text)
		return summary

q=Reader
url="https://en.wikipedia.org/wiki/cat"
#theres=q.fres("https://en.wikipedia.org/wiki/cat")
#q.test(theres)
text=q.scraptext(url,"cAt")
summary=q.summarisecontent(text)
print("the text length is")
print(len(text))
print(summary)
print(len(summary))




'''
# Tokenize the text into sentences and words
sentences = sent_tokenize(text)
words = word_tokenize(text)

# Remove stop words and stem the remaining words
stop_words = set(stopwords.words("english"))
ps = PorterStemmer()
filtered_words = [ps.stem(w) for w in words if not w in stop_words]

# Count the frequency of each word
word_freq = {}
for word in filtered_words:
    if word in word_freq:
        word_freq[word] += 1
    else:
        word_freq[word] = 1

# Calculate the score of each sentence based on the frequency of its words
sent_scores = {}
for sentence in sentences:
    for word in word_tokenize(sentence):
        if ps.stem(word) in word_freq:
            if sentence in sent_scores:
                sent_scores[sentence] += word_freq[ps.stem(word)]
            else:
                sent_scores[sentence] = word_freq[ps.stem(word)]

# Get the top 2 sentences with the highest scores as the summary
summary_sentences = sorted(sent_scores, key=sent_scores.get, reverse=True)[:2]
summary = " ".join(summary_sentences)
'''

'''
summary = summarize(text)

# Print the summary
print("this is the summary")
print(summary)

print("len of summary is ",len(summary))
print(summary)
print("len of actual content is ",len(text))
print("len of the summary is",len(summary))

'''


'''
import requests
from bs4 import BeautifulSoup

# Wikipedia page URL
#url = "https://en.wikipedia.org/wiki/Python_(programming_language)"

# Send an HTTP GET request to the URL and store the response
response = requests.get(url)

# Create a BeautifulSoup object from the HTML content
soup = BeautifulSoup(response.content, "html.parser")

# Extract the main body content of the Wikipedia page
main_content = soup.find("div", {"id": "mw-content-text"})

# Extract only the paragraphs from the main content
paragraphs = main_content.find_all("p")

# Concatenate the text content of all paragraphs
text = ""
for p in paragraphs:
    text += p.get_text()

# Print the extracted text
print("wikipedia text is")
print(text)
'''