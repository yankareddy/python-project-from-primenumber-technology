import requests
from bs4 import BeautifulSoup

# Send a GET request to the website
url = 'https://qcpi.questcdn.com/cdn/posting/?group=1950787&provider=1950787'
response = requests.get(url)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')

# Find the search postings section
search_postings = soup.find('div', {'id': 'search-postings'})

# Find the first 5 postings under the search postings section
postings = search_postings.find_all('div', {'class': 'row-fluid'})[:5]

# Extract and print the required fields for each posting
for posting in postings:
    est_value_notes = posting.find('div', {'class': 'estvalue-notes'}).text.strip()
    description = posting.find('div', {'class': 'desc'}).text.strip()
    closing_date = posting.find('div', {'class': 'closing-date'}).text.strip()

    print("Est. Value Notes:", est_value_notes)
    print("Description:", description)
    print("Closing Date:", closing_date)
    print()
