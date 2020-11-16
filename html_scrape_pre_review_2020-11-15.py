# -*- coding: utf-8 -*-
"""
Created on Thu Nov 12 15:12:48 2020

@author: ponde

Scraping HTML rendered websites

This code takes 1 input, which is a CSV file with columns to indicate:
    1 - Target URL
    2 - Method to scrape (html -> this code, js -> selenium code)
    3 - How to iterate thruought the website pages

"""


import pandas as pd
import requests
import datetime
from bs4 import BeautifulSoup

# This function will help us keep the code from stoping when we try a url with problems
def getResponse(url):
    
    check = True
    try:
        response = requests.get(url, timeout=(3.05, 27))
    except:
        check = False
        response = 'it did not work bro'

    return check, response


# saves html file of each iteration within a url
def saveHTML(soup,companyName,iteration):
    
    fileName = companyName + ' ' + str(iteration) + '.html'
    with open(r'C:\Users\ponde\Documents\programacao\Python\2020\JobHunt\JobHunt Project\input records' + fileName, "w",encoding='utf-8') as file:
        file.write(str(soup))  
    
# build data frame - the df arg is the input csv file as a dataframe
def dfBuilderV2(df):
    
    # initializing a DF
    columns = ['company','url','aTag','aTagText','aTagContent','href','keys', 'attributes', 'key_attr']
    dfFull = pd.DataFrame(columns=columns)
    
    # running the code for each company in the input df
    for i in range(len(df.index)):
        
        # if there is a last page for the url, we will build multiple urls for that company
        if df['lastPage'][i] != 'na':
            urls = buildURLs(df['company'][i],df['link'][i])
        else:
            urls = []
            urls.append(df['link'][i])
        
        # initializing a variable to save each iteration on the page as a html file (audit purposes)
        count = 0
        
        # iterating through all urls for the company
        for url in urls:
        
            check, response = getResponse(url)

            if check:

                # Parsing website
                soup = BeautifulSoup(response.text, "html.parser")

                # saving HTML
                saveHTML(soup,df['company'][i],count)

                # collecting "a" tags with hrefs
                links = soup.find_all("a", href=True)

                # Building initial DataFrame and Columns
                size = len(links)

                companies = [df['company'][i]]*size
                url = [url]*size
                aTagsText = []
                aTagsContent = []
                hrefs = []
                keys = []
                attributes = []
                key_attr = []

                # populating lists of data
                for link in links:
                    hrefs.append(link.get('href'))
                    aTagsText.append(str(link))
                    aTagsContent.append(link.text)
                    attributes.append(link.attrs.values())
                    keys.append(link.attrs.keys())
                    key_attr.append(link.attrs)
                    
                # Populating df
                data = {'company':companies,'url':url,'aTag':links,'aTagText':aTagsText,'aTagContent':aTagsContent,'href':hrefs,'keys':keys, 'attributes':attributes, 'key_attr':key_attr}
                dfTemp = pd.DataFrame(data)
                
                # count to name the file saved
                count += 1
            
            frames = [dfFull,dfTemp]
            dfFull = pd.concat(frames,ignore_index=True)
    
    return dfFull

# function to iterate thru pages (I know this is not the most beautiful code ever)

def buildURLs(company,url):
    urls = []
    if company == 'scotiabank':
        for i in range(25,225,25):
            finalURL = url + '&startrow=' + str(i)
            urls.append(finalURL)
    if company == 'Ernest & young':
        for i in range(1,20,1):
            finalURL = url + 'page' + str(i)
            urls.append(finalURL)
    if company == 'ADP':
        for i in range(1,4,1):
            finalURL = url + '&pg=' + str(i)
            urls.append(finalURL)
    if company == 'Facebook':
        for i in range(1,14,1):
            finalURL = url + '?page=' + str(i) + '&results_per_page=100&offices[0]=Altoona%2C%20IA&offices[1]=Ashburn%2C%20VA&offices[2]=Atlanta%2C%20GA&offices[3]=Austin%2C%20TX&offices[4]=Boston%2C%20MA&offices[5]=Chicago%2C%20IL&offices[6]=Dallas%2C%20TX&offices[7]=DeKalb%2C%20IL&offices[8]=Denver%2C%20CO&offices[9]=Detroit%2C%20MI&offices[10]=Eagle%20Mountain%2C%20Utah&offices[11]=Forest%20City%2C%20NC&offices[12]=Fort%20Worth%2C%20TX&offices[13]=Fremont%2C%20CA&offices[14]=Gallatin%2C%20TN&offices[15]=Henrico%2C%20VA&offices[16]=Huntsville%2C%20AL&offices[17]=Los%20Angeles%2C%20CA&offices[18]=Los%20Lunas%2C%20NM&offices[19]=Menlo%20Park%2C%20CA&offices[20]=Miami%2C%20Florida&offices[21]=Montreal%2C%20Canada&offices[22]=Mountain%20View%2C%20CA&offices[23]=New%20Albany%2C%20OH&offices[24]=New%20York%2C%20NY&offices[25]=Newton%20County%2C%20GA&offices[26]=Northridge%2C%20CA&offices[27]=Papillion%2C%20NE&offices[28]=Pittsburgh%2C%20PA&offices[29]=Prineville%2C%20OR&offices[30]=Redmond%2C%20WA&offices[31]=Remote%2C%20US%20Eastern%2C%20Mountain%20%26%20Central%20Regions&offices[32]=Remote%2C%20US%20Western%2C%20Mountain%20%26%20Central%20Regions&offices[33]=Reston%2C%20VA&offices[34]=San%20Francisco%2C%20CA&offices[35]=Santa%20Clara%2C%20CA&offices[36]=Sausalito%2C%20CA&offices[37]=Seattle%2C%20WA&offices[38]=Sunnyvale%2C%20CA&offices[39]=Toronto%2C%20Canada&offices[40]=Vancouver%2C%20Canada&offices[41]=Washington%2C%20DC#search_result'
            urls.append(finalURL)
    if company == 'Cisco':
        for i in range(0,50,25):
            finalURL = url + '&projectOffset=' + str(i)
            urls.append(finalURL)
    return urls


# Main

# reads companies and URLs to scrape
dfInput = pd.read_csv(r'C:\Users\ponde\Documents\programacao\Python\2020\JobHunt\JobHunt Project\inputCompanies - js rendered.csv',sep=';')

# filtering companies that are JS rendered (those require selenium for scraping)
dfInput = dfInput[dfInput['type']=='html']

# fixing the index after filtering the df
newIndex = [*range(len(dfInput.index))]
dfInput['newIndex'] = newIndex
dfInput.set_index('newIndex',inplace=True)

# filling the NaN values
dfInput['pagesCut'] = dfInput['pagesCut'].fillna('na')
dfInput['lastPage'] = dfInput['lastPage'].fillna('na')
dfInput['iterable'] = dfInput['iterable'].fillna('na')


# scraping and building the dataframe

dfFull = dfBuilderV2(dfInput)

# saving raw data

now = datetime.datetime.now()
today = datetime.datetime.today()

date = today.strftime("%Y-%m-%d")
hour = now.strftime("%H")
minute = now.strftime("%M")

stamp = str(date) + ' ' + str(hour) + 'h' + str(minute)

dfFull.to_csv(r'C:\Users\ponde\Documents\programacao\Python\2020\JobHunt\JobHunt Project\scraped_links_html '+str(stamp)+'.csv',index=False)
