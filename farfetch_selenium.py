from selenium import webdriver
import time
import re
import pandas as pd
import csv

# ff = pd.read_csv(r'C:\Users\BGCNHK\Desktop\farfetch\farfetch_combine.csv')
# list_urls = ff['url'].tolist()

df_farfetch = pd.read_csv('C:\\Users\\BGCNHK\\Desktop\\farfetch\\farfetch.csv')
ff_url = df_farfetch['url']
list_ff = []
page_num = len(df_farfetch)
for i in range(page_num):
    list_ff += ff_url[i].split(',')

# len(list_ff)
list_urls = list_ff

# pd.read_csv('farfetch.csv')

# Windows users need to specify the path to chrome driver you just downloaded.
# You need to unzip the zipfile first and move the .exe file to any folder you want.
# driver = webdriver.Chrome(r'path\to\the\chromedriver.exe')
driver = webdriver.Chrome(r'C:\Users\BGCNHK\Desktop\chromedriver.exe')
# Go to the page that we want to scrape

csv_file = open('farfetch_selenium_1.csv', 'w', encoding='utf-8', newline='')
writer = csv.writer(csv_file)


for i,url in enumerate(list_urls):
    print("Scraping product page number:", i)
    
    driver.get(url)
    try:
        price = driver.find_element_by_xpath('//span[@data-tstid="priceInfo-original"]').text
    except: 
        continue
    try:
        title = driver.find_element_by_xpath('//span[@dir="ltr"]').text
    except:
        continue
    try:
        subtitle = driver.find_element_by_xpath('//*[@id="bannerComponents-Container"]/span').text
    except:
        continue
    try:
        desc = driver.find_element_by_xpath('//p[@data-tstid="fullDescription"]').text
    except:
        continue
    try:
        made = driver.find_element_by_xpath('//p[@data-tstid="madeIn"]').text
    except:
        continue
    try:
        material = driver.find_element_by_xpath('//p[@ class="_373b06"]').text
    except:
        continue
    try:
        style_id = driver.find_element_by_xpath('//p[@data-tstid="designerStyleId"]/span').text
    except:
        continue
    # ff_id = driver.find_element_by_xpath('//p[@class="_b9c8b1" and @data-tstid="contactUs-id"]').text

    bag_dict = {}

    bag_dict['price'] = price
    bag_dict['title'] = title
    bag_dict['subtitle'] = subtitle
    bag_dict['desc'] = desc
    bag_dict['made'] = made
    bag_dict['material'] = material
    bag_dict['style_id'] = style_id
    # bag_dict['ff_id'] = ff_id
    
    writer.writerow(bag_dict.values())


# # Click review button to go to the review section
# review_button = driver.find_element_by_xpath('//span[@class="padLeft6 cursorPointer"]')
# review_button.click()

# # Page index used to keep track of where we are.
# index = 1
# # We want to start the first two pages.
# # If everything works, we will change it to while True
# while index <=2:
#   try:
#       print("Scraping Page number " + str(index))
#       index = index + 1
#       # Find all the reviews. The find_elements function will return a list of selenium select elements.
#       # Check the documentation here: http://selenium-python.readthedocs.io/locating-elements.html
#       reviews = driver.find_elements_by_xpath('//div[@class="row border_grayThree onlyTopBorder noSideMargin"]')
#       # Iterate through the list and find the details of each review.
#       for review in reviews:
#           # Initialize an empty dictionary for each review
#           review_dict = {}
#           # Use try and except to skip the review elements that are empty. 
#           # Use relative xpath to locate the title.
#           # Once you locate the element, you can use 'element.text' to return its string.
#           # To get the attribute instead of the text of each element, use 'element.get_attribute()'
#           try:
#               title = review.find_element_by_xpath('.//div[@class="NHaasDS75Bd fontSize_12 wrapText"]').text
#           except:
#               continue

#           print('Title = {}'.format(title))

#           # OPTIONAL: How can we deal with the "read more" button?
            
#           # Use relative xpath to locate text, username, date_published, rating.
#           # Your code here

#           # Uncomment the following lines once you verified the xpath of different fields
            
#           # review_dict['title'] = title
#           # review_dict['text'] = text
#           # review_dict['username'] = username
#           # review_dict['date_published'] = date_published
#           # review_dict['rating'] = rating

#       # We need to scroll to the bottom of the page because the button is not in the current view yet.
#       driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

#       # Locate the next button element on the page and then call `button.click()` to click it.
#       button = driver.find_element_by_xpath('//li[@class="nextClick displayInlineBlock padLeft5 "]')
#       button.click()
#       time.sleep(2)

#   except Exception as e:
#       print(e)
#       driver.close()
#       break