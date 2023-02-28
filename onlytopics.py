import requests
from bs4 import BeautifulSoup

# Get user input for topic
topic = input("Enter a topic to search for on the webpage: ")

# Send HTTP GET request to webpage and parse HTML content
#url = "https://google.com"  # replace with desired webpage URL
url="https://en.wikipedia.org/wiki/dog"
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# Loop through all links on webpage and check for relevant content
for link in soup.find_all('a'):
    # Send HTTP GET request to linked page and parse HTML content
    href = link.get('href')
    try:
        if href.startswith('http'):
            try:
                linked_page = requests.get(href)
                linked_soup = BeautifulSoup(linked_page.content, 'html.parser')

                # Check if linked page contains relevant content
                if topic in linked_soup.get_text():
                    print(href)
            except:
                print("not in link")
    except:
        pass        
