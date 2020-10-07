from bs4 import BeautifulSoup as bs
import requests

import utils

# Return a dictionary object for every cocktail on page
def get_page_data(req_link):
  src = requests.get(req_link).text
  soup = bs(src, 'html.parser')

  # Find table with class_ = 'infobox
  tables = soup.find_all('table', class_='infobox')
  if not tables:
    return

  cocktails = []

  for i in range(0, len(tables)):
    cocktail = {}

    # link
    cocktail['link'] = req_link

    # Name
    name = tables[i].find('caption')
    if name is None:
      continue
    else: cocktail['name'] = name.get_text()

    # Type
    type_of_cocktail = tables[i].find("th", string="Type")
    if type_of_cocktail is None: 
      cocktail['type'] = 'Null'
    else: cocktail['type'] = type_of_cocktail.parent.contents[-1].get_text()
    
  # IBA Official?
    iba_official = (tables[i].find_all("tr"))[0].get_text()
    if iba_official == 'IBA official cocktail':
      cocktail['iba_official'] = True
    else: cocktail['iba_official'] = False

    # Ingredients
    components = {}
    if (iba_official == 'IBA official cocktail'):
      if tables[i].find("a", string="IBA") is None:
        continue 
      else: ingredients = tables[i].find("a", string="IBA").parent.parent
    else: 
      if tables[i].find("th", string="Commonly used ingredients") is None:
        continue
      else: ingredients = tables[i].find("th", string="Commonly used ingredients").parent

    if ingredients is None: 
      cocktail['ingredients'] = 'Null'
    else: 
      for ing in ingredients.find_all('li'):
        components[ing.get_text()] = None
        # components[i.contents[1].get_text()] = i.contents[0]
    cocktail['ingredients'] = components
    
    # Primary alchohol by vol
    primary_alcohol = tables[i].find("th", string="Primary alcohol by volume")
    if primary_alcohol is None or primary_alcohol.parent.find('a') is None: 
      cocktail['primary_alcohol'] = 'Null'
    else: cocktail['primary_alcohol'] = primary_alcohol.parent.find('a').get_text()

    # Served
    served = tables[i].find("th", string="Served")
    if served is None: 
      cocktail['served'] = 'Null'
    else: cocktail['served'] = served.parent.find_all()[1].get_text()

    # Standard drinkware
    standard_drinkware = tables[i].find("th", string="Standard drinkware")
    if standard_drinkware is None: 
      cocktail['standard_drinkware'] = 'Null'
    else: cocktail['standard_drinkware'] = standard_drinkware.parent.contents[-1].get_text()
    

    # Standard garnish
    standard_garnish = tables[i].find("th", string="Standard garnish")
    if standard_garnish is None: 
      cocktail['standard_garnish'] = 'Null'
    else: cocktail['standard_garnish'] = standard_garnish.parent.find('td').get_text()

    # Preparation
    preparation = tables[i].find("th", string="Preparation")
    if preparation is None: 
      cocktail['preparation'] = 'Null'
    else: cocktail['preparation'] = preparation.parent.find('td').get_text()

    # picture link
    picture = tables[i].find("a", class_='image')
    if picture is None: 
      cocktail['picture'] = 'Null'
    else: cocktail['picture'] = picture.find('img')['src']

    # history
    
  
    cocktails.append(cocktail)
  return cocktails


# result = get_page_data('https://en.wikipedia.org/wiki/Joe_Gilmore#Four_Score_(1955)')
# result = get_page_data('https://en.wikipedia.org/wiki/Paradise_(cocktail)')
# get_page_data('https://en.wikipedia.org/wiki/Pisco_sour')
# get_page_data('https://en.wikipedia.org/wiki/Espresso_martini')
# get_page_data('https://en.wikipedia.org/wiki/B-52_(cocktail)')
# result = (get_page_data('https://en.wikipedia.org/wiki/Champagne_cocktail'))
# get_page_data('https://en.wikipedia.org/wiki/Astro_pop_(cocktail)')
# result = get_page_data('https://en.wikipedia.org/wiki/Springbokkie')
# result = get_page_data('https://en.wikipedia.org/wiki/Blueberry_Tea')
# result = get_page_data('https://en.wikipedia.org/wiki/Intus')
# result = get_page_data('https://en.wikipedia.org/wiki/Aviation_cocktail')

# if not result:
# 	print('None')
# else: 
# 	for i in result:
# 		utils.pretty(i)
# 		print('----------------------')

# print(result)
