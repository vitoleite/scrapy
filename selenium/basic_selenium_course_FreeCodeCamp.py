from time import sleep
from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Caso o caminho do driver do navegador esteja fora da pasta do script
# driver = webdriver.Chrome("C:\Program Files (x86)\chromedriver.exe")

links = ['https://demoqa.com/modal-dialogs', 'http://automationpractice.com/index.php', 'http://www.seleniumframework.com/Practiceform/']

# Caso o caminho do driver do navegador esteja dentro da pasta do script
browser = Chrome()
url = "https://demoqa.com/modal-dialogs"
browser.get(url)
browser.implicitly_wait(3)

my_element = browser.find_element(By.ID, 'showSmallModal')
my_element.click()

WebDriverWait(browser, 30).until(
    EC.text_to_be_present_in_element(
        (By.CLASS_NAME, 'modal-body'), # Element filtration
        'This is a small modal. It has very less content'# The expected text
    )
)

# my_element_2 = browser.find_element(By.CLASS_NAME, 'modal-body')
# print(f'Texto presente: {my_element_2.text}')


# browser.quit()