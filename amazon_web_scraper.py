from bs4 import BeautifulSoup
import pprint
import requests
import string
import time
import additional_files

URL = additional_files.URL
headers = additional_files.headers
dict_for_shirt = {"Head Title": '', 'Price': '', 'Rating': '', 'Timestamp' : ''}

page = requests.get(URL, headers=headers)
soup1 = BeautifulSoup(page.content, "html.parser")
soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

def creating_a_timestamp():
    ''' 
    This function creates a timestamp
        
    The purpose of this which gives us the date and time the page was scraped. The benefits 
    of creating this method is that the timestamp to be dynamic, rather than being a stationary
    value. This is then added to the dictionary for the t_shirt
    '''
    t = time.localtime()
    timestamp =  time.strftime('%Y-%m-%d %H:%M:%S', t)
    dict_for_shirt['Timestamp'] = timestamp
    return timestamp

def get_shirt_details():
    
    '''This method extracts all the relevant information and stores it in a dictionary'''

    title = soup2.find(id='productTitle').get_text().strip()
    dict_for_shirt['Head Title'] = title
    price = soup2.find('span', attrs = {'class':'a-offscreen'}).get_text().strip()
    dict_for_shirt['Price'] = price
    rating = soup2.find('span', attrs = {'class':'a-icon-alt'}).get_text().strip()
    dict_for_shirt['Rating'] = rating
    return title, price, rating

def display_info():

    ''' This function display the dictionary in which our scraped information is stored in  '''
    
    pprint.pprint(dict_for_shirt)

def extract_and_display_info():
    get_shirt_details()
    creating_a_timestamp()
    display_info()

extract_and_display_info()
