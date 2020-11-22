# -*- coding: utf-8 -*-
"""
Created on Sun Nov 12 19:39:07 2020

@author: ponde

Title: Scraping js rendered career websites

This code takes 1 input, which is a CSV file with columns to indicate:
    1 - Target URL
    2 - Method to scrape (html -> this code, js -> selenium code)

"""


from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

import datetime
import time

# # Function to Save the HTML file (audit purposes)
def saveHTML(soup,companyName,iteration):
    
    now = datetime.datetime.now()
    today = datetime.datetime.today()
    
    date = today.strftime("%Y-%m-%d")
    hour = now.strftime("%H")
    minute = now.strftime("%M")
    
    stamp = str(date) + ' ' + str(hour) + 'h' + str(minute)

    fileName = companyName + ' - ' + str(stamp) + ' ' + str(iteration) + '.html'
    with open(r'C:\Users\ponde\Documents\programacao\Python\2020\JobHunt\JobHunt Project\input records' + fileName, "w",encoding='utf-8') as file:
        file.write(str(soup))  


# # Getting the input data (website to scrape)

dfInput = pd.read_csv(r'C:\Users\ponde\Documents\programacao\Python\2020\JobHunt\JobHunt Project\inputCompanies - js rendered.csv',sep=';')

# Filtering only js rendered websites
dfJS = dfInput[dfInput['type']=='js'].copy()

# Fixing the index
newIndex = [*range(len(dfJS.index))]
dfJS['newIndex'] = newIndex
dfJS.set_index('newIndex',inplace=True)


# Declaring final DF
columns = ['company','url','aTag','aTagText','aTagContent','href','keys', 'attributes', 'key_attr']
dfFinal = pd.DataFrame(columns=columns)


# # Scraping the website

# Path to the cromedriver - this is the file that will enable python to control your chrome
PATH = "C:\Program Files (x86)\chromedriver.exe"

# Iterates through
for i in range(len(dfJS.index)):
    
    driver = webdriver.Chrome(PATH)
    
    site = dfJS['link'][i]
    
    driver.get(site)
    
    # This will allow the website to load the data before we proceed.
    time.sleep(15)

    aTag = []
    aTagsText = []
    aTagsContent = []
    hrefs = []
    keys = []
    attributes = []
    key_attr = []

    try:

        html_source = driver.page_source
        
        # now that we already loaded the page, we can proceed using beautifulsoup
        soup = BeautifulSoup(html_source, "html.parser")
        
        # we need to eventually create a function to iterate pages, but for now let's go this way
        iteration = 0
        saveHTML(soup,dfJS['company'][i],iteration)
        
        links = soup.find_all('a')
        
        size = len(links)
        
        
        for link in links:
            hrefs.append(link.get('href'))
            aTagsText.append(str(link))
            aTagsContent.append(link.text)
            attributes.append(link.attrs.values())
            keys.append(link.attrs.keys())
            key_attr.append(link.attrs)
            
        companies = [dfJS['company'][i]]*size
        url = [site]*size
        
        data = {'company':companies,'url':url,'aTag':links,'aTagText':aTagsText,'aTagContent':aTagsContent,'href':hrefs,'keys':keys, 'attributes':attributes, 'key_attr':key_attr}
        dfTemp = pd.DataFrame(data)
        
        frames = [dfFinal,dfTemp]
        dfFinal = pd.concat(frames,ignore_index=True)
        

    except:
        driver.quit()
    driver.quit()


dfLinks = dfFinal.copy()

# checking companies that did not load

target_companies = list(set(dfJS['company']))
reached_companies = list(set(dfLinks['company']))

missing_companies = []

for target in target_companies:
    if target not in reached_companies:
        missing_companies.append(target)

print(missing_companies)


## Saving the raw data
now = datetime.datetime.now()
today = datetime.datetime.today()

date = today.strftime("%Y-%m-%d")
hour = now.strftime("%H")
minute = now.strftime("%M")

stamp = str(date) + ' ' + str(hour) + 'h' + str(minute)

dfLinks.to_csv(r'C:\Users\ponde\Documents\programacao\Python\2020\JobHunt\JobHunt Project\scraped_links_js '+str(stamp)+'.csv',index=False)


