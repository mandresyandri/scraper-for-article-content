from bs4 import BeautifulSoup
import requests 
import re
from os.path import exists
import models
import sqlite3

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

# the update data
update_date = re.sub("Updated", "", splited[1])
update_date = re.sub("^\s+", '', update_date)

# the text content 
content = []
for content_text in soup.findAll(class_="Paragraph__component"):
    content.append(content_text.get_text())
content = ''.join(content)

# Bonus => image content 
images = []
#for image in soup.find_all(class_="Image__image"):
for image in soup.find_all("img"):
    images.append(image.get('src'))

# image treatment => No Blur + Size 
cleaned_img = []
for link in images:
    link = re.sub("e_blur:500", "e_blur:0", link)
    link = re.sub("w_50", "w_634", link)
    link = re.sub("h_28", "h_357", link)
    cleaned_img.append(link)


# if db doesn't existe => Create database [file : models.py]
in_file = exists('andri-database.db')
if in_file == False:
    print(models.create_models)
else: 
    pass

# dictionnary to structure data
scraped_data = {
    "title" : title, 
    "author" : author,
    "date_update": update_date,
    "image": cleaned_img[0],
    "content": content
}

# adding to db 
conn = sqlite3.connect('andri-database.db')
cursor = conn.cursor()

cursor.execute("""SELECT title, author, date_update, image, content FROM scraped_data""")
rows = cursor.fetchall()
print(type(rows))

# Adding to database : I have to verify if data exists => No action; If not in db => add content
# cursor.execute("""
# INSERT INTO scraped_data(title, author, date_update, image, content) VALUES(:title, :author, :date_update, :image, :content)""", scraped_data)
# conn.commit()


