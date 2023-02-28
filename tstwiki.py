import wikipedia

# Get user input for topic query
topic = input("Enter a topic to search for on Wikipedia: ")
print(topic)

# Search Wikipedia for topic and get page summary
try:
    page = wikipedia.page(topic)
    summary = page.content
except wikipedia.exceptions.DisambiguationError as e:
    # If the search term is ambiguous, get the first option
    page = wikipedia.page(e.options[0])
    summary = page.content

# Print the page summary
print(summary)
