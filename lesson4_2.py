from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    button_Submit = browser.find_element(By.CSS_SELECTOR, "button.trollface")
    button_Submit.click()

    browser.switch_to.window(browser.window_handles[1])
    
    x_element = browser.find_element(By.ID,"input_value")
    x = x_element.text
    print(x)
    y=calc(x)
    print(y)
    answer = browser.find_element(By.ID,"answer")
    answer.send_keys(y)

    button_Submit = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button_Submit.click()
finally:
    print(browser.switch_to.alert.text)
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()   
 
       