import sys
import get_listings
import get_page_data
import utils
  

def run_scrapper():
  print('<<<<< Scrapper starting >>>>>')

  cocktail_links = get_listings.get_listings('https://en.wikipedia.org/wiki/List_of_cocktails')

  utils.create_json([])
  for count, link in enumerate(cocktail_links):
    # progess bar
    sys.stdout.write('\r{0}'.format(count) + '/' + str(len(cocktail_links)) + ' pages scrapped: ' + link)
    sys.stdout.flush()
    # # time.sleep(random.randint(1,2)) # controls scrape rate so we dont flood the site with requests
    
    page_data = get_page_data.get_page_data(link)

    if not page_data or page_data is None:
      continue
    for i in page_data:
      utils.write_to_json(i)

    
  print('<<<<< Scraper completed >>>>>')
  
run_scrapper()
