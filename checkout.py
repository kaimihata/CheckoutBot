from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path=r"/Users/kaimihata/Desktop/CheckoutBot/chromedriver")
driver.get("https://www.supremenewyork.com/shop/all/pants")
items = driver.find_elements_by_xpath(".//a[contains(text(), 'Champion')]")
colors = []
for item in items:
    colors.append(item.get_attribute("href"))

item_paths = []
for color in colors:
    item_paths.append(driver.find_elements_by_xpath(".//a[contains(@href, " + "'" + color[30:] + "'" + ")]"))
 
for item_path in item_paths:
    print(item_path[2].get_attribute("text") + ": " + item_path[2].get_attribute("href")[30:])

driver.get(item_paths[0][2].get_attribute("href"))
#s_code = driver.find_element_by_xpath("//option[text() = 'Small']").get_attribute("value")
#m_code = driver.find_element_by_xpath("//option[text() = 'Medium']").get_attribute("value")
l_code = driver.find_element_by_xpath("//option[text() = 'Large']").get_attribute("value")
xl_code = driver.find_element_by_xpath("//option[text() = 'XLarge']").get_attribute("value")
token = driver.find_element_by_xpath("//meta[@name ='csrf-token']").get_attribute("content")
code = driver.find_element_by_xpath("//form[@id ='cart-addf']").get_attribute("action")
print("Large: " +  l_code)
print("XLarge: " + xl_code)
print("Token: " + token)
print("Code: " + code)
