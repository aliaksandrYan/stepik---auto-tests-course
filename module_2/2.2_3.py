import math
from selenium import webdriver
import time
import os


link = "http://suninjuly.github.io/file_input.html"
browser = webdriver.Chrome()
browser.get(link)



inputName = browser.find_element_by_xpath('//input[@name="firstname"]')
inputName.send_keys("Super name")

inputSurname = browser.find_element_by_xpath('//input[@name="lastname"]')
inputSurname.send_keys("Super lastname")

inputEmail = browser.find_element_by_xpath('//input[@name="email"]')
inputEmail.send_keys("Super email")


current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
file_path = os.path.join(current_dir, 'superFile.txt')


fileInput = browser.find_element_by_id("file")
fileInput.send_keys(file_path)

button = browser.find_element_by_css_selector("button.btn")
button.click()


time.sleep(10)
browser.quit()