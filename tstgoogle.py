from googlesearch import search
import requests
from bs4 import BeautifulSoup

# Get user input for query
query = input("Enter a query to search on Google: ")

# Search Google for query and get top 5 results
results = []
for result in search(query, num_results=5):
    results.append(result)

print(results)

response=requests.get(results[0])
soup=BeautifulSoup(response.content, 'html.parser')
# Extract content from HTML
content=soup.find_all('p')
# Print content
print('Content from:',results[0])
for p in content:
    print(p.text)
'''
# Loop through top results and scrape content
for result in results:
    # Get page HTML
    response = requests.get(result)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Extract content from HTML
    content = soup.find_all('p')

    # Print content
    print('Content from:', result)
    for p in content:
        print(p.text)
'''
