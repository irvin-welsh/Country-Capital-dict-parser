import time
from selenium import webdriver
import requests

xpaths=[] # create an empty list to store all pointers to data we're looking for


driver = webdriver.Chrome('/bin/chromedriver')  # initialize webdriver
URL="https://www.thoughtco.com/capitals-of-every-independent-country-1434452" # assign target URL to the variable URL
driver.get(URL) # recieve target webpage, using selenium
time.sleep(2) # imitates real user :)

def getAllXpaths():           # function receives all pointers (xpath(-es)) to our target data and adds up to the xpaths[] list
    for li_i in range(1,197):   # hardcoded range determined with chrome developer tools
        xpath = "/html/body/main/article/div[4]/div[1]/div[7]/ol/li[{}]".format(li_i)
        xpaths.append(xpath)
    return xpaths

def getCapitalsList(data): # function recieves xpaths[] list and parse its data to create a final list [Country, Capital]
    country_capitals=[]    # create an empty list to store [Country, Capital]
    for data in range(len(xpaths)):     # iterate over the xpaths[] list to fetch its data
        capitals = driver.find_element_by_xpath(str(xpaths[data])).text    # get text content from each xpath in the list
        formatted_capitals = capitals.split(": ") # important to split not only by a semicolon, but additionally with a space after it, to get correct list items
        country_capitals.append(formatted_capitals)   # insert correctly formatted data to the country_capitals[] list
        geo_dictionary = dict(country_capitals) # creating a dictionary object which will be reused in Quiz Master
    results_file = open("parsed.txt", 'w')        # make a file just to save the output and not to bother our target URL anytime when Quiz Master is running
    results_file.write(str(geo_dictionary)) # simple format of the file input
    results_file.close()    # ending up with a file
    return country_capitals

getAllXpaths()
getCapitalsList(xpaths)
driver.quit()               # closing webdriver (browser)
