import math
from selenium import webdriver
import time


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "https://suninjuly.github.io/execute_script.html"
browser = webdriver.Chrome()
browser.get(link)

x_element = browser.find_element_by_id("input_value")
x = x_element.text
y = calc(x)

inputField = browser.find_element_by_id("answer")
inputField.send_keys(y)

checkbox = browser.find_element_by_id("robotCheckbox")
checkbox.click()

radio = browser.find_element_by_id("robotsRule")
browser.execute_script("return arguments[0].scrollIntoView(true);", radio)
radio.click()

button = browser.find_element_by_css_selector("button.btn")
button.click()


time.sleep(10)
browser.quit()