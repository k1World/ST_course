from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math



def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


browser = webdriver.Chrome()

browser.get("https://suninjuly.github.io/explicit_wait2.html")

button1 = browser.find_element_by_css_selector("#book")


price = WebDriverWait(browser, 15).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100"))



button1.click()


input_val = browser.find_element_by_css_selector("#input_value.nowrap")
x = input_val.text

y = calc(x)

fme = browser.find_element_by_css_selector("#answer")
fme.send_keys(y)
button2 = browser.find_element_by_css_selector("#solve")
button2.click()


time.sleep(10)
browser.quit()