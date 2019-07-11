import math
from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select

link = "http://suninjuly.github.io/selects1.html"
browser = webdriver.Chrome()
browser.get(link)

num1 = browser.find_element_by_id("num1")
x = int(num1.text)

num2 = browser.find_element_by_id("num2")
y= int(num2.text)

sum = x + y

select = Select(browser.find_element_by_id("dropdown"))
select.select_by_value(str(sum))


button = browser.find_element_by_css_selector("button.btn")
button.click()


time.sleep(10)
browser.quit()