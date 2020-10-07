from bs4 import BeautifulSoup as bs
import requests

import utils

def get_listings(req_link):
  # Get all links 
  src = requests.get(req_link).text
  soup = bs(src, 'html.parser')

  # initialize set so that we dont have duplicate links
  links = set()

# find all divs with href attributes  
  listings_div = soup.find('div', class_='mw-parser-output')
  link = soup.find_all('a', href=True)
  for i in link:
    link_string = i['href']
    if link_string.startswith('/wiki/') and not utils.filtered_link(link_string):
      links.add('https://en.wikipedia.org' + link_string)

      # get page data here. Add link to wiki here as well.

  return links



  
