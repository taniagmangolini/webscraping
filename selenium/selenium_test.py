from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get('https://quotes.toscrape.com')

print(driver.current_url)
print(driver.title)

contents = driver.find_elements(By.CSS_SELECTOR,'.text')

for content in contents:
    print(content.text)

driver.close()
driver.quit()