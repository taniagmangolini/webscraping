from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get('https://quotes.toscrape.com')
print(driver.current_url)
print('Title:', driver.title)

# Login form
driver.find_element(By.CSS_SELECTOR,'.header-box p a').click()

username = driver.find_element(By.CSS_SELECTOR,'#username')
username.send_keys('ABC')

password = driver.find_element(By.CSS_SELECTOR,'#password')
password.send_keys('123456')

# Login button
driver.find_element(By.CSS_SELECTOR,'[value="Login"]').click()

driver.close()
driver.quit()