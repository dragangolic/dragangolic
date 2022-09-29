# import Necessary Libraries
from bs4 import BeautifulSoup as bs
import requests


# Load the web page content
r = requests.get("https://en.wikipedia.org/wiki/The_Good,_the_Bad_and_the_Ugly")

# Convert to a beautiful soup object
soup = bs(r.content)

# Print out the HTML
content = soup.prettify()
print(content)

# Start using Beautiful Soup to Scrape
first_header = soup.find("h1")
headers = soup.find_all("h1")
print(headers)

# Pass in a list of elements to look for
# first_header = soup.find("h1", "h2")
headers = soup.find_all("h1", "h2")
print(headers)

# Pass in attributes to the find/find_all function
paragraph = soup.find_all("p", attrs={"id": "paragraph-id"})
print(paragraph)

# You can nest find/find_all calls
body = soup.find('body')
div = body.find('div')  # narrowing down big pages
header = div.find('h1')
print(header)

# We can search specific strings in our find/find_all calls

paragraphs = soup.find_all("p", string={"Some bold text"})
print(paragraphs)
# import re if we want to find just the string
headers = soup.find_all("h2", string=re.compile("H|h"eader"))
# print(headers)

# select (CSS selector)
