from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)  
   
    price = WebDriverWait(browser,10).until(EC.text_to_be_present_in_element((By.ID,"price"),"$100"))
    button_Book = browser.find_element(By.ID, "book")    
    button_Book.click()
    
    browser.execute_script("window.scrollBy(0,150);")
 
    x_element = browser.find_element(By.ID,"input_value")
    x = x_element.text
    print(x)
    y=calc(x)
    print(y)
    answer = browser.find_element(By.ID,"answer")
    answer.send_keys(y)

    button_Submit = browser.find_element(By.ID, "solve")
    button_Submit.click()
finally:
    print(browser.switch_to.alert.text)
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    #time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()   
 
       