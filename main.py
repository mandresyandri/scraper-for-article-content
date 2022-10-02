from bs4 import BeautifulSoup
import requests 
import re
from os.path import exists
import models

# starter pack BS4 + requests
url = "https://edition.cnn.com/travel/article/scenic-airport-landings-2020/index.html"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# getting the title element 
title = soup.find('h1').getText()

# getting author + update and separate
author_and_update = soup.find(class_="Article__subtitle").get_text()

splited = author_and_update.split('CNN •')

# the author data 
author = re.sub(",", '', splited[0])

#the update data
update_date = re.sub("Updated", "", splited[1])
update_date = re.sub("^\s+", '', update_date)

# if db doesn't existe => Create database [file : models.py]
in_file = exists('andri-database.db')
if in_file == False:
    print(models.create_models)
else: 
    pass

# adding scrapped data in database 
