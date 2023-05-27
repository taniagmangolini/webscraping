from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get('https://quotes.toscrape.com')

print(driver.current_url)
print(driver.title)

pages_counter = 1
quotes_counter = 0
while True:
    quotes = driver.find_elements(By.CSS_SELECTOR,'.quote')
    for quote in quotes:
        print('-------------------------------------------------')
        quotes_counter += 1
        print('QUOTE:', quote.find_element(By.CSS_SELECTOR,'.text').text)
        print('AUTHOR:', quote.find_element(By.CSS_SELECTOR,'.author').text)
        for tag in quote.find_elements(By.CSS_SELECTOR,'.tag'):
            print('TAG:', tag.text)
            print('-------------------------------------------------')
    print(f'Total page quotes: {len(quotes)}')
         
    try:
        # Navigates to the next page clicking on the next button
        driver.find_element(By.CSS_SELECTOR,'.next a').click()
        pages_counter += 1
    except Exception as e:
        break

print(f'Total pages {pages_counter}.')
print(f'Total quotes {quotes_counter}.')

driver.close()
driver.quit()