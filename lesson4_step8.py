from selenium import webdriver
import math
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.support.ui import Select

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/explicit_wait2.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    text = WebDriverWait(browser, 25).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "100")
    )
    button = browser.find_element_by_id("book")
    button.click()
    x_control = browser.find_element_by_id("input_value")
    x = x_control.text
    y = calc(x)
    input = browser.find_element_by_id("answer")
    input.send_keys(y)
    button = browser.find_element_by_id("solve")
    button.click()
    
finally:
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()