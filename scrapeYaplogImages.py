#!/usr/bin/env python

#################################################################
#    2.12.2019                        Author: Michaela Honkova  #
#################################################################
#                                                               #
#    This script for Python 3 downloads full images             #
#    from entered Yaplog.jp blog, for blogs where /image/       #
#    folder is available. The images will be saved              #
#    into script's folder in image<post>-<num>-big.<ext>        #
#    format. Please set up following variables before you       #
#    run the script:                                            #
#                                                               #
                                                                
blog = 'http://yaplog.jp/milukyun'                              
postMin = 1           #first post to scrape                     
postMax = 158+1       #last post to scrape +1                   
                                                                
#                                                               #
#################################################################

#import requests
from bs4 import BeautifulSoup
from pathlib import Path
import os.path
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys   
import urllib.request

#set up 
directory = Path(__file__).parents[0]
options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument("--test-type")
options.add_argument('--ignore-ssl-errors')
options.add_argument('--ignore-certificate-errors-spki-list')
prefs = {'download.default_directory' : str(directory)}
options.add_experimental_option('prefs', prefs)
driver = webdriver.Chrome(options=options)  

#loop
#while True: 
for num in range(postMin, postMax):
    url = blog+'/image/'+str(num) +'/1' 
    
    #get webpage    
    driver.get(url)    
    body    = driver.page_source
    cookies = driver.get_cookies()

    #parse webpage
    soup = BeautifulSoup(body, 'html.parser')
    post = soup.find('div', {'class':'clearfix side-image-area'}) 
    if post != None:          
        
        #get thumbnail image webpage links    
        images = post.find_all('a', href=True)
        ImgIndex = 1
        for image in images:  
          
            #get image webpage
            print('Opening ' +str(image['href']))
            driver.get(image['href'])    
            body    = driver.page_source
            cookies = driver.get_cookies()
        
            #parse image webpage
            soup = BeautifulSoup(body, 'html.parser')
            part = soup.find('div', {'class':'main-image-area'}) 
            link = part.find('img')['src']
            if 'http' not in link:
                link = 'https:' +link
            
            #save image
            ext = link[-4:] 
            fName = 'image'+'{:04d}'.format(num)+'-'+'{:02d}'.format(ImgIndex) +'-big' +str(ext)
            print('Saving ' +fName)            
            fName = os.path.join(directory, fName)                                  
            try:
                urllib.request.urlretrieve(link, fName)
            except: #http error  404
                print("Error at image download! ", sys.exc_info()[0])
                continue            
            ImgIndex += 1

input('Finished scraping. Press <Enter> to END.')
driver.quit()
