import json

# Filters links based on blacklist. Returns true if link matches any substrings.
def filtered_link(link):
  blacklist = ['/Wikipedia:', '/Category:', '/Special:', '/Help:', '/Portal:',
               '/Main_Page', '/Talk:', 'List_of_', '/Category:', '/Template', 
               '/Lists_of_', '/History_of_', '/File:', '/IBA_Official_Cocktail']
  return any(x in link for x in blacklist)


def pretty(d, indent=0):
   for key, value in d.items():
      print('\t' * indent + str(key))
      if isinstance(value, dict):
         pretty(value, indent+1)
      else:
         print('\t' * (indent+1) + str(value))


def create_json(data, filename): 
  with open(filename,'w') as f: 
    json.dump(data, f, indent=4) 

def write_to_json(cocktail_data, filename):
  with open(filename) as json_file: 
    data = json.load(json_file) 
    data.append(cocktail_data) 
  create_json(data, filename)  


def get_number_of_recipes(filename):
  with open(filename) as json_file: 
    data = json.load(json_file) 
    print(len(data))
  
def clean_json_data():
  create_json([], 'cleaned_data.json')
  with open('data.json') as json_file: 
    data = json.load(json_file) 

    # remove listings without ingreedients
    for i in data:
      # print(data[i])
      if not i['ingredients']:
        print(i)
      else: write_to_json(i, 'cleaned_data.json')
    # remove duplicates by name and ingreedients

    # CandySenp1!




# clean_json_data()
get_number_of_recipes("data.json")
get_number_of_recipes('cleaned_data.json')
