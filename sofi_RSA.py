import os
from lib2to3.pgen2 import driver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from time import sleep
from dotenv import load_dotenv

# Load ENV
load_dotenv()

ACCOUNT_NAMES = os.getenv('ACCOUNT_NAMES').split(',')

SOFI_EMAIL = os.getenv('SOFI_EMAIL')
SOFI_PASSWORD = os.getenv('SOFI_PASSWORD')

def getDriver():
    chrome_options = Options()
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    try:
        driver = webdriver.Chrome(
                service=Service(ChromeDriverManager(cache_valid_range=30).install()),
                options=chrome_options)
    except Exception as e:
        try:
            driver = webdriver.Chrome(options=chrome_options)
        except Exception as ek:
            print(f'Attempted to use webdriver manager, but failed.')

    driver.maximize_window()
    return driver

driver = getDriver()
Ticker = input("Enter Stock TIKR: ")

# For testing:
#TIKR = 'SNES'

driver.get(f'https://www.sofi.com/wealth/app/stock/{Ticker}/buy')
sleep(3)
driver.find_element(By.XPATH, '//*[@id="username"]').send_keys(SOFI_EMAIL)
driver.find_element(By.XPATH, '//*[@id="password"]').send_keys(SOFI_PASSWORD)
driver.find_element(By.XPATH, '//*[@id="widget_block"]/main/section/div/div/div/form/div[2]/button').click()

driver.find_element(By.XPATH, '//*[@id="code"]').send_keys(input('Enter code: '))
driver.find_element(By.XPATH, '//*[@id="verifyCode"]').click()
sleep(5)

for account in ACCOUNT_NAMES:
    print(f'Purchasing {Ticker} for account: {account}')
    accounts = Select(driver.find_element(By.ID, 'dropdown-1'))
    accounts.select_by_visible_text(account)
    driver.find_element(By.XPATH, '//*[@id="input-4"]').send_keys('1')

    driver.find_element(By.XPATH, '//*[@id="mainContent"]/div/div[6]/button').click()
    sleep(1000)
    driver.find_element(By.XPATH, value='//*[@id="mainContent"]/div/div[4]/button[1]').click()

    driver.get(f'https://www.sofi.com/wealth/app/stock/{Ticker}/buy')