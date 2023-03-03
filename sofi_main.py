import sys
import os
import traceback
from time import sleep
from lib2to3.pgen2 import driver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from dotenv import load_dotenv

import sys

if len(sys.argv) < 3:
    print("Please provide the following arguments in order:")
    print("1. 'buy' or 'sell'")
    print("2. Stock Ticker (e.g. AAPL)")
    print("Optional: 'slow' and the wait time in seconds (e.g. slow 30)")
    print("\nExamples:")
    print("python main.py buy AAPL")
    print("python main.py sell AAPL")
    print("python main.py buy AAPL 100.54 slow 30")
    sys.exit(1)

TYPE = sys.argv[1].lower()
if 'buy' in TYPE:
    TYPE = 'buy'
elif 'sell' in TYPE:
    TYPE = 'sell'
else:
    print(f"Error: Invalid command '{sys.argv[1]}'")
    sys.exit(1)

STOCK = sys.argv[2].upper()

SLEEP_TIMER = False
try:
    if len(sys.argv) >= 3:
        LIMIT = sys.argv[3]
    print("TYPE:", TYPE)
    print("STOCK:", STOCK)
    print("LIMIT:$", LIMIT)
except:
    pass
try:
    if sys.argv[4].lower() == 'slow':
        try:
            SLEEP_TIMER = int(sys.argv[5])
        except:
            SLEEP_TIMER = 5
    print("SLEEP_TIMER:", SLEEP_TIMER)
except:
    print('Sleep timer not set.')


# Load ENV
load_dotenv()

ACCOUNT_NAMES = os.getenv('SOFI_ACCOUNT_NAMES').split(',')
EXCLUDE_ACCOUNTS = os.getenv('EXCLUDE_ACCOUNTS').split(',')

SOFI_LOGIN = os.getenv('SOFI_LOGIN')

colonIndex = SOFI_LOGIN.index(":")+1
EMAIL = SOFI_LOGIN[0:colonIndex-1]
PASSWORD = SOFI_LOGIN[colonIndex:len(SOFI_LOGIN)]
URL = f'https://www.sofi.com/wealth/app/stock/{STOCK}/{TYPE}'

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
    return driver

def login(driver):
    sleep(3)
    driver.find_element(By.XPATH, '//*[@id="username"]').send_keys(EMAIL)
    driver.find_element(By.XPATH, '//*[@id="password"]').send_keys(PASSWORD)
    driver.find_element(By.XPATH, '//*[@id="widget_block"]/main/section/div/div/div/form/div[2]/button').click()

    driver.find_element(By.XPATH, '//*[@id="code"]').send_keys(input('Enter code: '))
    driver.find_element(By.XPATH, '//*[@id="verifyCode"]').click()
    sleep(5)
    
def order(driver):
    fail = ''
    success = ''
    for account in ACCOUNT_NAMES:
        if account in EXCLUDE_ACCOUNTS:
            continue
        try:
            driver.get(URL)
            print(f'Purchasing {STOCK} for account:\t\t{account}')
            sleep(10)
            try:
                accounts = Select(driver.find_element(By.ID, 'dropdown-1'))
            except:
                try:
                    accounts = Select(driver.find_element(By.XPATH, value = '//*[@id="dropdown-1"]'))
                except:
                    accounts = Select(driver.find_element(By.XPATH, value = '/html/body/div/main/div/div[1]/select'))
            try:
                accounts.select_by_value(account)
            except:
                accounts.select_by_visible_text(account)
            sleep(5)
            try:
                try:
                    driver.find_element(By.XPATH, value = f"//button[contains(.,'Shares')]").click()
                except:
                    driver.find_element(By.XPATH, value = f'//*[@id="shares"]').click()
            except:
                pass
            sleep(5)
            try:
                driver.find_element(By.XPATH, '//*[@id="input-4"]').send_keys('1')
            except:
                driver.find_element(By.XPATH, value = '//*[@id="input-8"]').send_keys('1')
            try:
                driver.find_element(By.XPATH, value = '//*[@id="input-8"]').send_keys(LIMIT)
            except:
                pass
            try:
                if TYPE == 'sell' and "hold shares" in driver.find_element(By.XPATH, value = '//*[@id="input-4"]').text.lower():
                    print(f'No shares to sell, skipping account:\t{account}.')
                    continue
            except:
                pass
            try:
                driver.find_element(By.XPATH, '//*[@id="mainContent"]/div/div[6]/button').click()
            except:
                driver.find_element(By.XPATH, value = "//button[contains(.,'Review')]").click()
            try:
                driver.find_element(By.XPATH, value = "/html/body/div[2]/div/div/div[3]/button[1]").click()
            except:
                pass
            if SLEEP_TIMER:
                sleep(SLEEP_TIMER)
            else:
                sleep(15)
            try:
                driver.find_element(By.XPATH, value='//*[@id="mainContent"]/div/div[4]/button[1]').click()
            except:
                try:
                    if TYPE == 'buy':
                        driver.find_element(By.XPATH, value = f"//button[contains(.,'Buy')]").click()
                    elif TYPE == 'sell':
                        driver.find_element(By.XPATH, value = f"//button[contains(.,'Sell')]").click()
                except:  
                    driver.find_element(By.XPATH, value = f"/html/body/div[1]/main/div/div[4]/button[1]").click()


            print(f'Successful {TYPE} {STOCK} for account:\t\t{account}\n\n')
            success += f'{account},'
            sleep(10)
        except Exception as e:
            print(traceback.format_exc())
            print(f'\n\n\nFailed to {TYPE} {STOCK} for account: {account}. Attempting to continue with next account.')
            fail += f'{account},'
            driver.get(URL)
    print(f'Failed to {TYPE} {STOCK} for accounts:\n{fail}\n\nSuccessfully {TYPE} {STOCK} for accounts:\n{success}')


def main():
    driver = getDriver()
    driver.get(URL)
    login(driver)
    
    order(driver)
    print('Program sucessfully completed')

if __name__ == '__main__':
    main()


    # Q: True or False: To execute a Switch Spoofing attack the intruder makes use of the  VLAN Registration protocol AND the Dynamic Trunking protocol AND must be in the same network.
    
