import time
from selenium import webdriver
import requests
result_dict={}
xpaths=[]

driver = webdriver.Chrome('/bin/chromedriver')  # Optional argument, if not specified will search pathself.
URL="https://www.thoughtco.com/capitals-of-every-independent-country-1434452"
driver.get(URL)
time.sleep(2) # Let the user actually see something!

def get_all_xpaths():
    for li_i in range(1,197):
        xpath = "/html/body/main/article/div[4]/div[1]/div[7]/ol/li[{}]".format(li_i)
        xpaths.append(xpath)
        li_i+=1
    return xpaths

def convert_list_to_dict(data):
    country_capitals=[]
    for data in range(len(xpaths)):
        capitals = driver.find_element_by_xpath(str(xpaths[data])).text
        # capitals.text
        capitals.split(":")
        country_capitals.append(capitals)
    print(country_capitals,len(country_capitals))
    results_file = open("parsed.txt", 'w')
    results_file.write(str(country_capitals)+'')
    results_file.close()

get_all_xpaths()
convert_list_to_dict(xpaths)
driver.quit()
