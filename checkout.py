import sys
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from seleniumrequests import Chrome

# Initializes the chromewebdriver
print(os.name)
if os.name == 'nt':
    driver = Chrome(executable_path=r"./windows/chromedriver.exe")
elif os.name == 'posix':
    driver = Chrome(executable_path=r"./osx/chromedriver")
r = driver.request('GET', 'https://www.google.com/')
keyword = "Casino"
usr_color = "Creen"
category = "jackets"
driver.get("https://www.supremenewyork.com/shop/all/" + category)
items = driver.find_elements_by_xpath(".//a[contains(text(), " + "'" + keyword + "'" + ")]")
colors = []
for item in items:
    colors.append(item.get_attribute("href"))

item_paths = []
for color in colors:
    item_paths.append(driver.find_elements_by_xpath(".//a[contains(@href, " + "'" + color[30:] + "'" + ")]"))

path = ""
for item_path in item_paths:
    if usr_color in item_path[2].get_attribute("text"):
        path = item_path[2].get_attribute("href")
if (path == ""):
    path = item_paths[0][2].get_attribute("href")

print("https://www.supremenewyork.com" + path)
driver.get(path)

size_codes = []
try:
    size_codes.append("S " + driver.find_element_by_xpath("//option[text() = 'Small']").get_attribute("value"))
except:
    e = sys.exc_info()[0]
try:
    size_codes.append("M " + driver.find_element_by_xpath("//option[text() = 'Medium']").get_attribute("value"))
except:
    e = sys.exc_info()[0]
try:
    size_codes.append("L " + driver.find_element_by_xpath("//option[text() = 'Large']").get_attribute("value"))
except:
    e = sys.exc_info()[0]
try:
    size_codes.append("X " + driver.find_element_by_xpath("//option[text() = 'XLarge']").get_attribute("value"))
except:
    e = sys.exc_info()[0]

token = driver.find_element_by_xpath("//meta[@name ='csrf-token']").get_attribute("content")
code = driver.find_element_by_xpath("//form[@id ='cart-addf']").get_attribute("action")
utf = "%E2%9C%93"

print(size_codes)
print("Token: " + token)
print("Code: " + code)
print("Code substr: " + code[36:42])
PARAMS = {'utf-8': utf,
          'X-CSRF-Token': token,
          'st': code[36:42],
          's': size_codes[0][2:],
          'commit': 'add to cart'}

r = driver.request('POST', code, PARAMS)

print(r)