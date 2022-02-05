from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

css_selectors_guide = 'https://www.w3schools.com/cssref/css_selectors.asp'

driver = Chrome()
url = "https://demoqa.com/automation-practice-form"
driver.get(url)
driver.implicitly_wait(5)
driver.maximize_window()

name = driver.find_element(By.ID, 'firstName')
last_name = driver.find_element(By.ID, 'lastName')

name.send_keys(Keys.NUMPAD0, Keys.NUMPAD0, Keys.NUMPAD7)
last_name.send_keys('Unexpected')

# Utilizando as Keys para descer até o final da página
# html = driver.find_element(By.TAG_NAME, 'html')
# html.send_keys(Keys.END)

try:
    driver.implicitly_wait(15)
    btn_ad = driver.find_element(By.CSS_SELECTOR, 'a[id="close-fixedban"]')
    btn_ad.click()
except:
    print('hide ad failed')
    driver.quit()

try:
    # Utilizando as Keys para descer até o final da página
    html = driver.find_element(By.TAG_NAME, 'html')
    html.send_keys(Keys.END)

    btn = driver.find_element(By.CSS_SELECTOR, 'button[id="submit"]')
    btn.click()
except:
    print('submit button failed')
    driver.quit()


try:
    btn_form_1 = driver.find_element(By.ID, 'hobbies-checkbox-1')
    btn_form_2 = driver.find_element(By.ID, 'hobbies-checkbox-2')
    btn_form_3 = driver.find_element(By.ID, 'hobbies-checkbox-3')
    btn_form_1.send_keys(Keys.SPACE)
    btn_form_2.send_keys(Keys.SPACE)
    btn_form_3.send_keys(Keys.SPACE)
except:
    print('Not worked, review path')