import requests
from bs4 import BeautifulSoup
import csv

# Collect page data 
page = requests.get('https://en.wikipedia.org/wiki/List_of_postal_codes_of_Canada:_M')
# Create a BeautifulSoup object
soup = BeautifulSoup(page.text, 'html.parser')

# Pull all text from the table
canada_postal_list = soup.find_all('table')[0]
# Pull td from all instances of <tr> tag within BodyText div
canada_postal_list_items = canada_postal_list.select('tbody > tr')

# Create a file to write to, add headers row
f = csv.writer(open('canada_postal_codes.csv', 'w'))
f.writerow(['Postal Code', 'Borough','Neighborhood'])

# Create for loop to print out all postal code data
for canada_postal_data in canada_postal_list_items[0:]:
    # print(state_data.prettify())
    # pull content out of tags
    # state = state_data.text
    postal_code = [th.text.rstrip() for th in canada_postal_data.find_all('td')]
    # print(state)
    f.writerow(postal_code)
