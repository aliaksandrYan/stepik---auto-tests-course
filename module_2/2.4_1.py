import math
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/explicit_wait2.html"
browser = webdriver.Chrome()
browser.get(link)

price = WebDriverWait(browser, 10).until(
        EC.text_to_be_present_in_element((By.ID, "price"),"10000")
    )

bron = browser.find_element_by_id("book")
bron.click()

x_element = browser.find_element_by_id("input_value")
x = x_element.text
y = calc(x)

inputField = browser.find_element_by_id("answer")
inputField.send_keys(y)

button = browser.find_element_by_id("solve")
button.click()


time.sleep(10)
browser.quit()